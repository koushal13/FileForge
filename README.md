# ⚡ FileForge

<div align="center">

**Universal File Converter - Web & Desktop**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/koushal13/FileForge)

</div>

A simple, powerful file converter with a clean web interface. Convert images and PDFs effortlessly.

## 🌐 **Quick Start - Web Version (Recommended)**

The easiest way to use FileForge is through the web interface:

```bash
# Install dependencies
pip install Pillow pillow-heif PyMuPDF flask

# Run the web app
python web_app.py
```

Then open your browser to **http://localhost:5000**

### ✨ Web Features
- 🖼️ **Image Converter**: HEIC, JPG, PNG, WebP, BMP, TIFF, GIF with quality control
- 📄 **Merge PDFs**: Combine multiple PDFs into one file
- ✂️ **Split PDF**: Extract individual pages as a ZIP archive
- 🗜️ **Compress PDF**: Reduce file size while maintaining quality

> **💡 Why Web Version?** Clean interface, works everywhere, no complex setup needed!


## 🖥️ Alternative: Desktop Version

For advanced features, you can also run the desktop application:

```bash
python fileforge_converter.py
```

## 📦 Installation

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/koushal13/FileForge.git
cd FileForge

# Install dependencies
pip install Pillow pillow-heif PyMuPDF flask

# Run web version (recommended)
python web_app.py
```

### Dependencies
- **Pillow** - Image processing engine
- **pillow-heif** - HEIC/HEIF support for iPhone photos
- **PyMuPDF** - PDF manipulation
- **Flask** - Web framework (for web version)

## 🎯 Features

### 🖼️ Image Conversion
- **Formats**: HEIC, HEIF, JPG, PNG, WebP, BMP, TIFF, GIF
- **Perfect for iPhone photos** - Convert HEIC to JPG instantly
- **Quality control** - Adjustable quality settings (1-100)
- **Auto-orientation** - Respects EXIF data
- **Transparency handling** - Smart conversion for formats without alpha channel

### 📄 PDF Tools
- **Merge**: Combine multiple PDFs into one document
- **Split**: Extract individual pages (downloaded as ZIP)
- **Compress**: Reduce file size with optimization

## 💡 Why FileForge?

✅ **Simple & Clean** - No cluttered interface, just what you need  
✅ **Web-Based** - Works in your browser, no complex installation  
✅ **Privacy** - All processing happens locally  
✅ **Fast** - Efficient conversion algorithms  
✅ **Free & Open Source** - MIT licensed

## 🏗️ Architecture Overview

### Core Components

#### **Professional Image Converter** (`professional_image_converter.py`)
- 6-checkpoint validation system for conversion integrity
- Real PIL/Pillow processing with pillow-heif for HEIC support
- Quality control and format validation
- Professional error handling and logging

#### **Main GUI Application** (`fileforge_converter.py`)
- Auto-maximized professional interface
- Tabbed organization for different conversion types
- Integrated professional converter for image processing
- Complete document processing suite
- Advanced batch processing with live updates

#### **Dependency Management** (`install_dependencies.py`)
- Automatic installation of all required libraries
- Graceful handling of missing dependencies
- Installation progress tracking and reporting

## 🛠️ Installation & Setup

### System Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 2GB RAM minimum, 4GB recommended for batch processing
- **Storage**: 100MB for application + space for converted files

### Quick Installation
```bash
# Clone the repository
git clone https://github.com/koushal13/SilentCanoe-FileForge.git
cd SilentCanoe-FileForge

# Install all dependencies automatically
python install_dependencies.py

# Launch the application
python fileforge_converter.py
```

### Manual Dependency Installation
```bash
# Core image processing
pip install Pillow>=10.0.0 pillow-heif>=0.13.0

# Document processing
pip install PyPDF2>=3.0.0 beautifulsoup4>=4.12.0 reportlab>=4.0.0

# Optional enhancements
pip install python-docx>=1.1.0 markdown>=3.5.0 html2text>=2020.1.16
```

### Dependencies Overview

#### **Required (Core Functionality)**
- `Pillow` - Professional image processing engine
- `pillow-heif` - HEIC/HEIF format support for iPhone photos
- `PyPDF2` - PDF manipulation and processing
- `beautifulsoup4` - HTML parsing and text extraction
- `reportlab` - PDF creation and document generation

#### **Optional (Enhanced Features)**
- `python-docx` - Microsoft Word document support
- `markdown` - Markdown processing capabilities
- `html2text` - Enhanced HTML to text conversion

## 💎 Professional Features

### 🔬 **6-Checkpoint Validation System**
1. **Input Validation**: Verify file format and integrity
2. **Format Verification**: Confirm output format compatibility
3. **Path Preparation**: Ensure output path accessibility
4. **Conversion Processing**: Execute actual image conversion
5. **Output Validation**: Verify successful file creation
6. **Integrity Check**: Final quality and corruption verification

### 📊 **Real-time Progress Tracking**
- Live conversion status updates
- File-by-file progress indication
- Statistical reporting (success/failure rates)
- Time estimation and completion forecasting
- Memory and performance monitoring

### 🔄 **Advanced Batch Operations**
- Multi-threaded processing for performance
- Intelligent file filtering and selection
- Recursive directory traversal
- Resumable operations (future enhancement)
- Error recovery and continuation

## 🎯 Use Cases

### 📱 **iPhone Photo Management**
Convert HEIC photos to JPG for universal compatibility:
```bash
python fileforge_converter.py
# Use the Image Converter tab for single conversions
# Use the Batch Processor tab for bulk operations
```

### 📄 **Document Processing**
Professional document operations:
- **PDF Merge**: Combine multiple PDFs into one
- **PDF Split**: Extract specific pages from documents
- **Format Conversion**: Convert between PDF, Text, HTML, Markdown
- **Text Processing**: Extract, count, find & replace text content

### 🔄 **Batch Media Processing**

## 🚀 Usage

### Web Version (Recommended)
```bash
# Start the server
python web_app.py

# Open in browser
# http://localhost:5000
```

**Features:**
- Upload and convert files instantly
- Download converted files directly
- Clean, simple interface
- Works on any device with a browser

### Desktop Version
```bash
# For advanced batch operations
python fileforge_converter.py
```

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with:
- [Pillow](https://python-pillow.org/) - Image processing
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF manipulation
- [Flask](https://flask.palletsprojects.com/) - Web framework

---

**Made with ❤️ for easy file conversion**
cd SilentCanoe-FileForge

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 📊 Performance Benchmarks

- **Image Conversion**: 5-50 files/second (format and size dependent)
- **Batch Processing**: Multi-threaded performance scaling
- **Memory Usage**: Optimized for large file processing
- **Validation Speed**: <100ms per checkpoint
- **GUI Responsiveness**: Non-blocking operations with threading

## 🔗 Links

- **Repository**: [GitHub](https://github.com/koushal13/SilentCanoe-FileForge)
- **Issues**: [Report Issues](https://github.com/koushal13/SilentCanoe-FileForge/issues)
- **Documentation**: [Full Docs](https://github.com/koushal13/SilentCanoe-FileForge/docs)
- **Website**: [SilentCanoe.com](https://silentcanoe.com)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pillow Team** - Excellent image processing foundation
- **pillow-heif Project** - HEIC/HEIF format support
- **PyPDF2 Developers** - PDF processing capabilities  
- **Open Source Community** - Inspiration and support

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://silentcanoe.com">SilentCanoe</a></strong><br>
  <em>Professional file conversion made simple</em><br><br>
  <img src="https://img.shields.io/badge/✨-Production%20Ready-brightgreen?style=for-the-badge" alt="Production Ready">
  <img src="https://img.shields.io/badge/🔧-Auto%20Setup-blue?style=for-the-badge" alt="Auto Setup">
  <img src="https://img.shields.io/badge/🚀-Professional%20GUI-purple?style=for-the-badge" alt="Professional GUI">
</p>

## 🚀 Quick Start - Try It Now!

### 🖥️ **GUI Demo** (Instant Launch)
```bash
python demo.py
```
- Professional file analyzer with drag-and-drop interface
- Interactive directory browser with file tree view
- Detailed file information reports with conversion suggestions
---

#### Convert Commands
```bash
# Image conversion
fileforge convert image input.heic output.jpg --quality 90 --resize 1920x1080

# Document conversion
fileforge convert document doc.pdf doc.docx --password secret

# Audio conversion
fileforge convert audio song.wav song.mp3 --quality high --normalize

# Video conversion
fileforge convert video movie.avi movie.mp4 --resolution 720p --quality medium
```

#### Batch Operations
```bash
# Batch convert with options
fileforge batch /path/to/images --to jpg --recursive --quality 85

# Specific file patterns
fileforge batch /photos --pattern "*.heic" --to png --threads 8
```

#### PDF Operations
```bash
# Merge PDFs
fileforge pdf merge file1.pdf file2.pdf file3.pdf merged.pdf

# Split PDF
fileforge pdf split document.pdf --pages 1-10,15-20

# Compress PDF
fileforge pdf compress large.pdf compressed.pdf --level high

# Encrypt PDF
fileforge pdf encrypt document.pdf secure.pdf --password mypassword

# Add watermark
fileforge pdf watermark input.pdf output.pdf "CONFIDENTIAL" --opacity 0.3
```

### Python API

```python
from fileforge import ConversionEngine

# Initialize engine
engine = ConversionEngine()

# Convert single file
success = engine.convert_single(
    'input.heic', 
    'output.jpg', 
    quality=90,
    resize=(1920, 1080)
)

# Batch conversion
results = engine.convert_batch(
    input_folder='photos',
    output_folder='converted',
    file_pattern='*.heic',
    output_format='jpg',
    recursive=True,
    quality=85
)

print(f"Converted {results['successful']}/{results['total']} files")
```

## 🛠️ Installation & Setup

### System Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 2GB RAM minimum, 4GB recommended
- **Storage**: 100MB for application + space for converted files

### Dependencies

#### Required (Auto-installed)
- `Pillow` - Image processing
- `pillow-heif` - HEIC/HEIF support
- `PyMuPDF` - PDF processing

#### Optional (Manual Installation)
- **FFmpeg** - Audio/video conversion ([Download](https://ffmpeg.org/download.html))
- **LibreOffice** - Office document conversion ([Download](https://www.libreoffice.org/download/))
- **Tesseract OCR** - Text recognition ([Download](https://github.com/tesseract-ocr/tesseract))
- **Pandoc** - Advanced document conversion ([Download](https://pandoc.org/installing.html))

### Platform-Specific Setup

#### Windows
```powershell
# Install using pip
pip install -r requirements.txt

# Optional: Install using Chocolatey
choco install ffmpeg libreoffice pandoc
```

#### macOS
```bash
# Install using Homebrew
brew install ffmpeg libreoffice pandoc tesseract

pip install -r requirements.txt
```

#### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt update
sudo apt install ffmpeg libreoffice pandoc tesseract-ocr

pip install -r requirements.txt
```

## 🎯 Use Cases

### 📱 **iPhone Photo Management**
- Convert HEIC photos to JPG for universal compatibility
- Batch process entire photo libraries
- Create thumbnails and contact sheets
- Resize images for web use

### 🏢 **Business Document Processing**
- Convert PDFs to editable Word documents
- Merge multiple documents into single PDFs
- Compress large files for email sharing
- Add watermarks and password protection

### 🎧 **Media Library Organization**
- Convert between audio formats for different devices
- Normalize audio levels across collections
- Extract audio from video files
- Compress media for storage optimization

### 🎬 **Content Creation**
- Convert videos for different platforms
- Create animated GIFs from videos
- Resize videos for social media
- Compress videos for faster uploads

## 🏗️ Architecture

### Project Structure
```
silentcanoe-fileforge/
├── fileforge/
│   ├── __init__.py
│   ├── core.py                 # Core processing engine
│   ├── converters/
│   │   ├── image_converter.py  # Image processing
│   │   ├── document_converter.py # PDF & documents
│   │   ├── audio_converter.py  # Audio processing
│   │   └── video_converter.py  # Video processing
│   ├── gui/
│   │   └── main.py            # GUI interface
│   └── cli/
│       └── main.py            # CLI interface
├── tests/                     # Test suite
├── docs/                      # Documentation
├── scripts/                   # Utility scripts
├── fileforge.py              # Main entry point
└── requirements.txt          # Dependencies
```

### Key Components

#### **ConversionEngine**
Central orchestrator that handles file type detection and routes conversions to appropriate converters.

#### **BatchProcessor**
Manages parallel processing of multiple files with progress tracking and error handling.

#### **Converter Modules**
Specialized processors for each file type with format-specific optimizations.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/silentcanoe/fileforge.git
cd fileforge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```

### Areas for Contribution
- **New Format Support**: Add support for additional file formats
- **Performance Optimization**: Improve conversion speed and memory usage
- **UI/UX Improvements**: Enhance the GUI and user experience
- **Documentation**: Improve docs, examples, and tutorials
- **Testing**: Expand test coverage and add integration tests
- **Internationalization**: Add support for multiple languages

## 📊 Performance

### Benchmarks
- **Image Conversion**: ~5-50 files/second (depending on size and format)
- **Document Processing**: ~1-10 documents/second
- **Audio Conversion**: ~10-100x real-time (depending on quality)
- **Video Processing**: ~0.5-5x real-time (depending on resolution and codec)

### Optimization Tips
- Use SSD storage for better I/O performance
- Increase thread count for batch operations on multi-core systems
- Use appropriate quality settings to balance size and speed
- Enable hardware acceleration when available (GPU encoding)

## 🔧 Troubleshooting

### Common Issues

#### "FFmpeg not found"
- **Solution**: Install FFmpeg and ensure it's in your system PATH
- **Download**: https://ffmpeg.org/download.html

#### "LibreOffice conversion failed"
- **Solution**: Install LibreOffice headless support
- **Command**: `sudo apt install libreoffice --no-install-recommends` (Linux)

#### "Out of memory" errors
- **Solution**: Process files in smaller batches or increase system RAM
- **Alternative**: Use lower quality settings for large files

#### Slow conversion speeds
- **Solution**: 
  - Use faster storage (SSD vs HDD)
  - Increase number of processing threads
  - Use hardware acceleration when available
  - Choose appropriate quality settings

### Debug Mode
```bash
# Enable verbose logging
export FILEFORGE_DEBUG=1
python fileforge.py convert image input.heic output.jpg
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pillow** team for excellent image processing capabilities
- **FFmpeg** project for comprehensive media processing
- **PyMuPDF** for powerful PDF manipulation
- **LibreOffice** for document conversion support
- **Open Source Community** for inspiration and contributions

## 📞 Support

- **Documentation**: [Full Documentation](https://github.com/silentcanoe/fileforge/docs)
- **Issues**: [GitHub Issues](https://github.com/silentcanoe/fileforge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/silentcanoe/fileforge/discussions)
- **Website**: [SilentCanoe.com](https://silentcanoe.com)

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://silentcanoe.com">SilentCanoe</a></strong><br>
  <em>Making file conversion effortless and powerful</em>
</p>