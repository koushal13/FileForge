#!/usr/bin/env python3
"""
FileForge Web Application
A simple web interface for file conversion
"""

from flask import Flask, render_template, request, send_file, flash, redirect, url_for, jsonify
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
import pillow_heif
import fitz  # PyMuPDF
import tempfile
import shutil
import pytesseract
import ollama

pillow_heif.register_heif_opener()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fileforge-secret-key-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

ALLOWED_IMAGE_EXTENSIONS = {'heic', 'heif', 'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp', 'gif'}
ALLOWED_PDF_EXTENSIONS = {'pdf'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert-image', methods=['POST'])
def convert_image():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    if not allowed_file(file.filename, ALLOWED_IMAGE_EXTENSIONS):
        flash('Invalid file type. Supported: HEIC, JPG, PNG, WebP, BMP, TIFF, GIF', 'error')
        return redirect(url_for('index'))
    
    try:
        output_format = request.form.get('format', 'jpg')
        quality = int(request.form.get('quality', 90))
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # Convert image
        output_filename = Path(filename).stem + f'.{output_format}'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        with Image.open(input_path) as img:
            img = ImageOps.exif_transpose(img)
            
            # Handle transparency for JPEG
            if output_format in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:
                    background.paste(img)
                img = background
            elif img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGB')
            
            # Save with quality settings
            save_kwargs = {}
            if output_format in ['jpg', 'jpeg']:
                save_kwargs = {'quality': quality, 'optimize': True, 'progressive': True}
            elif output_format == 'png':
                save_kwargs = {'optimize': True}
            elif output_format == 'webp':
                save_kwargs = {'quality': quality}
            
            img.save(output_path, **save_kwargs)
        
        # Clean up input file
        os.remove(input_path)
        
        # Send file and clean up after
        return send_file(output_path, as_attachment=True, download_name=output_filename)
        
    except Exception as e:
        flash(f'Conversion failed: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/merge-pdf', methods=['POST'])
def merge_pdf():
    if 'files' not in request.files:
        flash('No files selected', 'error')
        return redirect(url_for('index'))
    
    files = request.files.getlist('files')
    if len(files) < 2:
        flash('Please select at least 2 PDF files', 'error')
        return redirect(url_for('index'))
    
    try:
        # Save uploaded files
        temp_files = []
        for file in files:
            if file and allowed_file(file.filename, ALLOWED_PDF_EXTENSIONS):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                temp_files.append(filepath)
        
        if len(temp_files) < 2:
            flash('Please upload valid PDF files', 'error')
            return redirect(url_for('index'))
        
        # Merge PDFs
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
        merged = fitz.open()
        
        for pdf_file in temp_files:
            doc = fitz.open(pdf_file)
            merged.insert_pdf(doc)
            doc.close()
        
        merged.save(output_path)
        merged.close()
        
        # Clean up temp files
        for filepath in temp_files:
            os.remove(filepath)
        
        return send_file(output_path, as_attachment=True, download_name='merged.pdf')
        
    except Exception as e:
        flash(f'Merge failed: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/split-pdf', methods=['POST'])
def split_pdf():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if not file or not allowed_file(file.filename, ALLOWED_PDF_EXTENSIONS):
        flash('Please upload a valid PDF file', 'error')
        return redirect(url_for('index'))
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # Create temp directory for split pages
        split_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'split_pages')
        os.makedirs(split_dir, exist_ok=True)
        
        # Split PDF
        doc = fitz.open(input_path)
        for page_num in range(doc.page_count):
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            output_file = os.path.join(split_dir, f'page_{page_num + 1:03d}.pdf')
            new_doc.save(output_file)
            new_doc.close()
        doc.close()
        
        # Create zip file
        import zipfile
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'split_pages.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in os.listdir(split_dir):
                zipf.write(os.path.join(split_dir, file), file)
        
        # Clean up
        os.remove(input_path)
        shutil.rmtree(split_dir)
        
        return send_file(zip_path, as_attachment=True, download_name='split_pages.zip')
        
    except Exception as e:
        flash(f'Split failed: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/compress-pdf', methods=['POST'])
def compress_pdf():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if not file or not allowed_file(file.filename, ALLOWED_PDF_EXTENSIONS):
        flash('Please upload a valid PDF file', 'error')
        return redirect(url_for('index'))
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # Compress PDF
        output_filename = Path(filename).stem + '_compressed.pdf'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        doc = fitz.open(input_path)
        doc.save(output_path, garbage=4, deflate=True, clean=True, linear=True)
        doc.close()
        
        # Clean up
        os.remove(input_path)
        
        return send_file(output_path, as_attachment=True, download_name=output_filename)
        
    except Exception as e:
        flash(f'Compression failed: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/ocr-image', methods=['POST'])
def ocr_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if not file or not allowed_file(file.filename, ALLOWED_IMAGE_EXTENSIONS):
        return jsonify({'error': 'Please upload a valid image file'}), 400
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # Open image and perform OCR
        img = Image.open(input_path)
        
        # Extract text using pytesseract
        text = pytesseract.image_to_string(img)
        
        # Clean up
        img.close()
        os.remove(input_path)
        
        if not text.strip():
            return jsonify({'text': '', 'message': 'No text detected in image'}), 200
        
        return jsonify({'text': text.strip()}), 200
        
    except pytesseract.TesseractNotFoundError:
        return jsonify({'error': 'Tesseract OCR is not installed. Please install it first.', 
                       'install_help': 'macOS: brew install tesseract | Linux: apt-get install tesseract-ocr | Windows: Download from github.com/UB-Mannheim/tesseract/wiki'}), 500
    except Exception as e:
        return jsonify({'error': f'OCR failed: {str(e)}'}), 500


@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'No text provided for analysis'}), 400
    
    try:
        prompt = f"""Analyze the following text extracted from an image and provide:
1. A brief summary of what the content is about
2. Identify if there are any issues, errors, warnings, or problems mentioned
3. Provide helpful recommendations or next steps if applicable

Extracted text:
{text.strip()}

Provide a concise, helpful analysis:"""
        
        response = ollama.chat(
            model='llama3.2:1b',  # Lightweight model
            messages=[{'role': 'user', 'content': prompt}]
        )
        ai_analysis = response['message']['content']
        
        return jsonify({'analysis': ai_analysis}), 200
        
    except Exception as e:
        error_msg = str(e)
        if 'connection' in error_msg.lower() or 'refused' in error_msg.lower():
            return jsonify({'error': 'Ollama is not running. Please start Ollama first.', 
                           'install_help': 'Install Ollama from ollama.com, then run: ollama pull llama3.2:1b'}), 500
        return jsonify({'error': f'AI analysis failed: {error_msg}'}), 500


if __name__ == '__main__':
    # For production, use gunicorn instead
    # gunicorn --bind 0.0.0.0:$PORT web_app:app
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
