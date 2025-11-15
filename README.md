# ⚡ FileForge

<div align="center">

### 🔒 **Privacy-First File Converter** 🚀

**Convert images • Manipulate PDFs • Extract text with AI**  
*All processing happens locally. Your files never leave your device.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Web-lightgrey)](https://github.com/koushal13/FileForge)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub issues](https://img.shields.io/github/issues/koushal13/FileForge)](https://github.com/koushal13/FileForge/issues)
[![GitHub stars](https://img.shields.io/github/stars/koushal13/FileForge?style=social)](https://github.com/koushal13/FileForge)

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Docs](#-installation) • [🗺️ Roadmap](ROADMAP.md) • [💬 Discussions](https://github.com/koushal13/FileForge/discussions)

</div>

---

## 🌟 Why FileForge?

**FileForge** is a free, open-source file conversion toolkit that puts **privacy first**. Unlike online converters that upload your files to unknown servers, FileForge processes everything **locally on your machine**.

✨ **Perfect for:**
- 📱 Converting iPhone HEIC photos to JPG
- 📄 Merging, splitting, and compressing PDFs
- 🔍 Extracting text from images with OCR
- 🤖 AI-powered document analysis (optional, local)

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

✅ **Privacy First** - All processing happens locally, files never leave your device  
✅ **100% Free & Open Source** - MIT licensed, free forever  
✅ **Simple & Clean** - Beautiful web interface, no clutter  
✅ **No Registration Required** - Just download and use  
✅ **AI-Enhanced** - Optional local AI analysis with Ollama  
✅ **Cross-Platform** - Works on macOS, Linux, and Windows

---

## 🤝 **Support This Project**

If FileForge saves you time, consider:
- ⭐ [**Star this repo**](https://github.com/koushal13/FileForge) to show your support
- 💰 [**Sponsor on GitHub**](https://github.com/sponsors/koushal13) to fund development
- 🐛 [**Report bugs**](https://github.com/koushal13/FileForge/issues) to help improve it
- 🔀 [**Contribute code**](CONTRIBUTING.md) to add features
- 📢 [**Share on Twitter**](https://twitter.com/intent/tweet?text=Check%20out%20FileForge%20-%20a%20privacy-first%20file%20converter!&url=https://github.com/koushal13/FileForge) to spread the word

---

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

---

## 🗺️ **What's Next?**

Check out our [**Roadmap**](ROADMAP.md) to see what's coming:
- 🎬 Video conversion support
- 🎵 Audio processing tools
- 🌐 Browser extensions
- 📱 Mobile apps
- 🔌 API endpoints

**Want a feature?** [Open an issue](https://github.com/koushal13/FileForge/issues) or join the [discussion](https://github.com/koushal13/FileForge/discussions)!

---

## 🤝 Contributing

We love contributions! Check out our [**Contributing Guide**](CONTRIBUTING.md) to get started.

**Ways to contribute:**
- 🐛 Fix bugs and report issues
- ✨ Add new features from the [roadmap](ROADMAP.md)
- 📖 Improve documentation
- 🎨 Design UI/UX improvements
- 🧪 Write tests and improve code quality

**Good first issues:** [Click here](https://github.com/koushal13/FileForge/labels/good%20first%20issue)

---

## 📊 **Project Stats**

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/koushal13/FileForge?style=social)
![GitHub forks](https://img.shields.io/github/forks/koushal13/FileForge?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/koushal13/FileForge?style=social)

</div>

---

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

---

## 📞 **Community & Support**

- 💬 [**GitHub Discussions**](https://github.com/koushal13/FileForge/discussions) - Ask questions, share ideas
- 🐛 [**Issue Tracker**](https://github.com/koushal13/FileForge/issues) - Report bugs, request features
- 📧 **Email** - Contact the maintainer for private inquiries
- 🐦 **Twitter** - Follow for updates (coming soon)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

**TL;DR:** You can use, modify, and distribute this software freely, even commercially.

---

## 🙏 Acknowledgments

Built with:
- [Pillow](https://python-pillow.org/) - Image processing
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF manipulation  
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Text extraction
- [Ollama](https://ollama.com/) - AI-powered analysis

---

---

<div align="center">

**⭐ If FileForge helped you, give it a star! ⭐**

**Made with ❤️ for privacy-focused file conversion**

[Star on GitHub](https://github.com/koushal13/FileForge) • [Report Bug](https://github.com/koushal13/FileForge/issues) • [Request Feature](https://github.com/koushal13/FileForge/issues/new) • [Sponsor](https://github.com/sponsors/koushal13)

</div>
