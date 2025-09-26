# 📸➡🔊 Intelligent Document Recognition & OCR Web Application

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-orange.svg)](https://github.com/tesseract-ocr/tesseract)
[![Google APIs](https://img.shields.io/badge/Google-Translate%20%26%20TTS-red.svg)](https://cloud.google.com/)

> *Transform any image containing text into natural speech in 100+ languages*

Extract text from images using advanced OCR technology, translate it to any language, and convert it to high-quality speech audio - all through an intuitive web interface.

## 🎯 *What This Project Does*

This Flask web application creates a complete *Image → Text → Speech pipeline*:

1. *📤 Upload* any image containing text (screenshots, photos, documents)
2. *🔍 Extract* text automatically using Tesseract OCR
3. *🌐 Detect* the language and translate to 100+ languages  
4. *🎵 Generate* natural speech audio using Google Text-to-Speech
5. *💾 Download* the MP3 audio file

## ✨ *Key Features*

### 🔍 *Advanced OCR Processing*
- *Tesseract OCR* integration with OpenCV preprocessing
- Supports *JPG, PNG, BMP, TIFF* image formats
- Automatic text extraction from any image
- Smart error handling for unclear images

### 🌍 *Multilingual Support*
- *Automatic language detection* of extracted text
- *100+ languages* supported for translation
- *Google Translate API* integration
- Support for major world languages including English, Spanish, French, German, Chinese, Japanese, Arabic, Hindi, and more

### 🎵 *Natural Speech Generation*
- *Google Text-to-Speech (gTTS)* for high-quality audio
- *MP3 format* output for universal compatibility
- *Instant playback* in the browser
- *Download functionality* for offline use

### 🎨 *Modern Web Interface*
- *Drag & drop* file upload with Dropzone.js
- *Bootstrap 4* responsive design
- *Lobster font* for elegant typography
- *Image carousel* showcasing OCR capabilities
- *Real-time processing* feedback

## 📸 *Screenshots*

### Homepage with Feature Carousel
The landing page features an elegant carousel showcasing OCR examples and easy access to upload functionality.

### OCR Results & Translation Interface
After uploading an image, users can review extracted text, see detected language, edit text if needed, and select target language for translation and speech generation.

### Audio Generation & Download
Generated speech audio can be played instantly in the browser and downloaded as MP3 for later use.

## 🚀 *Quick Start*

### *Prerequisites*
- Python 3.7+
- Tesseract OCR installed on your system

### *Installation*

1. *Clone the repository*
bash
git clone https://github.com/yourusername/ocr-to-speech-converter.git
cd ocr-to-speech-converter


2. *Install Tesseract OCR*
bash
# Ubuntu/Debian
sudo apt update && sudo apt install tesseract-ocr tesseract-ocr-eng

# macOS
brew install tesseract

# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki


3. *Create virtual environment*
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


4. *Install Python dependencies*
bash
pip install -r requirements.txt


5. *Create required directories*
bash
mkdir -p static/images static/uploaded_files static/audio_files flask_session


6. *Add sample carousel images* (optional)
Add 3 demo images to static/images/:
- image_01.jpg
- image_02.png  
- image_03.jpg

7. *Run the application*
bash
python run.py


8. *Open your browser* and navigate to http://127.0.0.1:5000

## 🏗 *Project Structure*


ocr-to-speech-converter/
│
├── application/
│   ├── __init__.py          # Flask app configuration with Dropzone
│   ├── routes.py            # Main routes: upload, OCR processing, audio generation
│   ├── forms.py             # WTForms for text editing and language selection
│   └── utils.py             # Google Translate & language detection utilities
│
├── templates/
│   ├── layout.html          # Base template with Bootstrap 4 & Lobster font
│   ├── index.html           # Homepage with carousel and feature buttons
│   ├── upload.html          # Dropzone file upload interface
│   └── decoded.html         # OCR results, translation form & audio player
│
├── static/
│   ├── images/              # Carousel demo images
│   ├── uploaded_files/      # Temporary image storage (auto-cleanup)
│   └── audio_files/         # Generated MP3 audio files
│
├── requirements.txt         # Python dependencies
├── run.py                  # Flask application entry point
└── README.md               # This documentation


## 🛠 *Technology Stack*

### *Backend*
- *Flask 2.3.3* - Lightweight web framework
- *Tesseract OCR* - Text extraction from images
- *OpenCV* - Image preprocessing for better OCR
- *Google Translate API* - Language detection and translation
- *Google Text-to-Speech* - Natural speech generation

### *Frontend*  
- *Bootstrap 4* - Responsive UI framework
- *Dropzone.js* - Drag & drop file uploads
- *Google Fonts (Lobster)* - Typography
- *SweetAlert* - Enhanced user notifications

### *Key Python Libraries*
- pytesseract - Tesseract OCR wrapper
- googletrans - Google Translate integration  
- gTTS - Google Text-to-Speech
- opencv-python - Image processing
- Flask-Dropzone - File upload handling
- Flask-WTF - Form handling and validation

## 📖 *How to Use*

### *Step 1: Upload Image*
1. Visit the homepage and click "Image To Text" or "Image To Audio"
2. Drag and drop an image or click to browse
3. Supported formats: JPG, PNG, BMP, TIFF (max 3MB)

### *Step 2: OCR Processing*
1. The system automatically extracts text using Tesseract OCR
2. Language is detected automatically
3. You'll be redirected to the results page

### *Step 3: Review & Edit*
1. Review the extracted text in the text area
2. Edit any OCR errors if needed
3. The detected language is displayed at the top

### *Step 4: Generate Audio*
1. Select target language from the dropdown
2. Click "Translate & Generate Audio"
3. Wait for processing (translation + speech generation)

### *Step 5: Listen & Download*
1. Audio plays automatically in the browser
2. Click "Download Audio" to save the MP3 file
3. Use "Upload Another Image" for additional conversions

## ⚙ *Configuration*

### *Tesseract Path Configuration*
The application automatically detects Tesseract installation. If needed, manually update in application/routes.py:

python
# Common paths:
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'        # Linux
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'   # macOS
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows


### *Flask Configuration*
Key settings in application/__init__.py:
- File upload size limit: 3MB
- Allowed file types: Images only
- Session management: Filesystem-based
- Dropzone styling and behavior

## 🔧 *Troubleshooting*

### *Common Issues*

*"Error processing image" message:*
- Ensure image has clear, readable text
- Try images with high contrast (dark text on light background)  
- Check that image file is not corrupted

*OCR not working:*
bash
# Test Tesseract installation
tesseract --version

# Find Tesseract location
which tesseract  # Linux/macOS
where tesseract  # Windows


*Translation/TTS errors:*
- Check internet connection (Google APIs required)
- Try with different text content
- Verify language is supported for TTS

*File upload issues:*
- Ensure file size is under 3MB
- Check file format is supported
- Verify upload directories exist and are writable

## 🎯 *Use Cases*

### *Accessibility*
- Convert printed documents to audio for visually impaired users
- Read signs and text aloud in foreign countries
- Transform physical books/papers into audio format

### *Language Learning*
- Hear pronunciation of foreign text in images
- Translate and listen to text in target language
- Practice with real-world text examples

### *Content Creation*
- Extract text from images for editing
- Generate voiceovers from visual content
- Create audio versions of visual materials

### *Research & Documentation*
- Digitize handwritten or printed notes
- Extract data from screenshots
- Create searchable content from images

## 📊 *Performance & Limitations*

### *Performance*
- *OCR Speed*: 2-5 seconds per image
- *Translation*: 1-2 seconds per text block  
- *Audio Generation*: 3-5 seconds for short texts
- *Supported Languages*: 100+ for translation, 60+ for TTS

### *Limitations*
- Image quality affects OCR accuracy
- Handwritten text has lower recognition rates
- Very small or blurry text may not be recognized
- Internet connection required for translation and TTS
- File size limited to 3MB

### *Best Results Tips*
- Use high-resolution images with good lighting
- Ensure text is horizontal and clearly visible
- High contrast works better (black text on white background)
- Avoid complex backgrounds behind text

## 🚀 *Deployment*

### *Local Development*
bash
python run.py
# Access at http://127.0.0.1:5000


### *Production Deployment*
For production deployment, consider:
- Using Gunicorn or uWSGI as WSGI server
- Setting up nginx reverse proxy
- Implementing proper logging
- Adding rate limiting for API calls
- Setting up HTTPS

## 🤝 *Contributing*

Contributions are welcome! Areas for improvement:
- Additional OCR engines (EasyOCR, PaddleOCR)
- Batch image processing
- User interface enhancements
- Additional audio formats
- Mobile app development

## 📄 *License*

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 *Author*

*[Pooja Gajjar]*
- GitHub: [@poojaa77](https://github.com/poojaa77)
- LinkedIn: [Your Profile](https://www.linkedin.com/in/pooja-gajjar-4bb121285/)

## 🙏 *Acknowledgments*

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for powerful text recognition
- [Google Cloud APIs](https://cloud.google.com/) for translation and speech services
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for responsive design
- [OpenCV](https://opencv.org/) for image processing capabilities

---

<div align="center">

*⭐ If this project helped you, please give it a star! ⭐*

*Perfect for portfolios showcasing data processing, computer vision, and full-stack development skills*

</div>

