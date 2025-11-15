# ⚡ FileForge

<div align="center">

**Simple Web-Based File Converter**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Web-lightgrey)](https://github.com/koushal13/FileForge)

</div>

A clean, simple web application for converting images, manipulating PDFs, and extracting text with AI-powered analysis.

## 🎥 Demo

https://private-user-images.githubusercontent.com/21079636/514679276-a78c1294-710f-406e-bf1d-56830a5305af.mov

## 🌐 **Quick Start**

```bash
# Clone the repository
git clone https://github.com/koushal13/FileForge.git
cd FileForge

# Install dependencies
pip install -r requirements.txt

# Run the web app
python web_app.py
```

Then open your browser to **http://localhost:5000**

## ✨ Features

- 🖼️ **Image Converter**: Convert HEIC, JPG, PNG, WebP, BMP, TIFF, GIF with quality control
- 🤖 **OCR + AI Analysis**: Extract text from images and get intelligent analysis with Ollama
- 📄 **Merge PDFs**: Combine multiple PDF files into one
- ✂️ **Split PDF**: Extract individual pages as separate PDFs (ZIP download)
- 🗜️ **Compress PDF**: Reduce PDF file size while maintaining quality

> **💡 Web-First Design**: Clean interface, works in any browser, privacy-focused (all processing happens locally)


## 📦 Installation

### Prerequisites
- **Python 3.9+** (tested on Python 3.9.6)
- **Tesseract OCR** (for text extraction feature)
- **Ollama** (optional, for AI-powered text analysis)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/koushal13/FileForge.git
cd FileForge

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

# Install Python dependencies
pip install -r requirements.txt

# Install Tesseract OCR (for OCR feature)
# macOS:
brew install tesseract

# Linux (Ubuntu/Debian):
sudo apt-get install tesseract-ocr

# Windows:
# Download from https://github.com/UB-Mannheim/tesseract/wiki

# Install Ollama (optional, for AI analysis)
# Download from https://ollama.com
# Then pull the lightweight model:
ollama pull llama3.2:1b

# Run the application
python web_app.py
```

### Dependencies
- **Pillow** (11.3.0) - Image processing engine
- **pillow-heif** (1.1.1) - HEIC/HEIF support for iPhone photos
- **PyMuPDF** (1.26.5) - PDF manipulation
- **Flask** (3.1.2) - Web framework
- **pytesseract** (0.3.13) - OCR text extraction
- **ollama** (0.6.1) - AI-powered text analysis (optional)

## 🎯 Feature Details

### 🖼️ Image Conversion
- **Supported Formats**: HEIC, HEIF, JPG, PNG, WebP, BMP, TIFF, GIF
- **Perfect for iPhone photos** - Convert HEIC to JPG/PNG instantly
- **Quality control** - Adjustable quality settings (1-100)
- **Auto-orientation** - Respects EXIF data
- **Transparency handling** - Smart conversion for formats without alpha channel

### 🤖 OCR + AI Text Analysis
- **Text Extraction**: Uses Tesseract OCR to extract text from images, screenshots, and scanned documents
- **AI-Powered Analysis**: Optional AI analysis using Ollama (llama3.2:1b model)
  - Summarizes extracted content
  - Identifies issues, errors, and warnings
  - Provides helpful recommendations
- **Two-Step Process**: Extract text first, then optionally analyze with AI
- **Privacy-Focused**: All processing happens locally on your machine

### 📄 PDF Tools
- **Merge**: Combine multiple PDFs into one document
- **Split**: Extract individual pages (downloaded as ZIP archive)
- **Compress**: Reduce file size with optimization while maintaining quality

## 💡 Why FileForge?

✅ **Simple & Clean** - No cluttered interface, just what you need  
✅ **Web-Based** - Works in your browser, accessible from any device  
✅ **Privacy First** - All processing happens locally on your machine  
✅ **Fast & Efficient** - Optimized conversion algorithms  
✅ **AI-Enhanced** - Optional intelligent text analysis with Ollama  
✅ **Free & Open Source** - MIT licensed

## 🚀 Usage

### Starting the Server
```bash
python web_app.py
```

The web interface will be available at **http://localhost:5000**

### Using the Features

#### Image Conversion
1. Go to the **Image Converter** tab
2. Select your image file (HEIC, JPG, PNG, etc.)
3. Choose output format and quality
4. Click **Convert Image**
5. Download your converted file

#### OCR + AI Analysis
1. Go to the **OCR** tab
2. Upload an image containing text
3. Click **Extract Text** to extract the text
4. Review the extracted text
5. (Optional) Click **🤖 Analyze with AI** to get intelligent analysis
6. Copy the text or use the analysis insights

**Note**: Make sure Ollama is running with the llama3.2:1b model for AI analysis:
```bash
ollama pull llama3.2:1b
ollama serve
```

#### PDF Operations
- **Merge**: Select multiple PDF files and combine them
- **Split**: Upload a PDF to extract all pages as separate files
- **Compress**: Upload a PDF to reduce its file size

## 🛠️ Technical Details

### Project Structure
```
FileForge/
├── web_app.py              # Flask web application
├── templates/
│   └── index.html          # Web interface (5 tabs)
├── static/
│   └── style.css          # Modern gradient styling
├── requirements.txt        # Python dependencies
├── archive/               # Legacy desktop app files
└── README.md
```

### Web Application (`web_app.py`)
- **Flask Routes**:
  - `/` - Main page with tabbed interface
  - `/convert-image` - Image format conversion
  - `/ocr-image` - OCR text extraction
  - `/analyze-text` - AI-powered text analysis
  - `/merge-pdf` - Combine multiple PDFs
  - `/split-pdf` - Extract PDF pages
  - `/compress-pdf` - Reduce PDF file size
- **Features**: File upload handling, temporary file management, error handling
- **AI Integration**: Ollama client for intelligent text analysis

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via [GitHub Issues](https://github.com/koushal13/FileForge/issues)
- Suggest new features
- Submit pull requests

## 🔧 Troubleshooting

### Common Issues

**"Tesseract not found" error**
- Install Tesseract OCR for your platform (see Installation section)
- Ensure it's in your system PATH

**"Ollama connection refused" or AI analysis not working**
- Make sure Ollama is installed and running: `ollama serve`
- Pull the required model: `ollama pull llama3.2:1b`
- AI analysis is optional - OCR will still work without it

**Port 5000 already in use**
```bash
# Kill the process using port 5000
lsof -ti:5000 | xargs kill -9
```

**Blank window on macOS (old desktop version)**
- Use the web version instead: `python web_app.py`
- The desktop GUI has known issues with macOS Tk

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with:
- [Pillow](https://python-pillow.org/) - Image processing
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF manipulation  
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Text extraction
- [Ollama](https://ollama.com/) - AI-powered analysis

---

**Made with ❤️ for simple, privacy-focused file conversion**