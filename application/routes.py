from application import app, dropzone
from flask import render_template, request, redirect, url_for, session, send_file
from .forms import QRCodeData
import secrets
import os

# OCR
import cv2
import pytesseract
from PIL import Image
import numpy as np
# pip install gTTS
from gtts import gTTS

# import utils
from . import utils


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        # set a session value
        sentence = ""
        
        f = request.files.get('file')
        if not f or not f.filename:
            return "No file uploaded", 400
            
        filename, extension = f.filename.rsplit(".", 1)
        generated_filename = secrets.token_hex(10) + f".{extension}"
       
        file_location = os.path.join(app.config['UPLOADED_PATH'], generated_filename)
        f.save(file_location)

        try:
            # OCR here - Try multiple possible Tesseract paths
            possible_paths = [r'C:\Users\POOJA\tesseract.exe']
            
            # Try to find tesseract
            import shutil
            tesseract_path = shutil.which('tesseract')
            if tesseract_path:
                pytesseract.pytesseract.tesseract_cmd = tesseract_path
            else:
                # Try predefined paths
                for path in possible_paths:
                    if os.path.exists(path):
                        pytesseract.pytesseract.tesseract_cmd = path
                        break

            print(f"Using Tesseract at: {pytesseract.pytesseract.tesseract_cmd}")

            img = cv2.imread(file_location)
            if img is None:
                raise Exception("Could not load image file")
                
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Try simple text extraction first
            try:
                boxes = pytesseract.image_to_data(img)
                print(f"OCR boxes data: {boxes[:200]}...")  # Debug print
            except Exception as ocr_error:
                print(f"Detailed OCR Error: {ocr_error}")
                # Try simple text extraction as fallback
                sentence = pytesseract.image_to_string(img)
                if sentence.strip():
                    session["sentence"] = sentence.strip()
                    return redirect("/decoded/")
                else:
                    raise Exception("No text found in image")
        
            for i, box in enumerate(boxes.splitlines()):
                if i == 0:
                    continue

                box = box.split()

                # only deal with boxes with word in it.
                if len(box) == 12:
                    sentence += box[11] + " "
           
            if not sentence.strip():
                # Fallback to simple text extraction
                sentence = pytesseract.image_to_string(img)
                
            session["sentence"] = sentence.strip() if sentence.strip() else "No text found in image. Please try with a clearer image containing readable text."

        except Exception as e:
            print(f"OCR Error: {e}")
            import traceback
            print(f"Full traceback: {traceback.format_exc()}")
            session["sentence"] = f"Error processing image: {str(e)}. Please try with a clearer image."
        
        finally:
            # delete file after you are done working with it
            if os.path.exists(file_location):
                os.remove(file_location)

        return redirect("/decoded/")

    else:
        return render_template("upload.html", title="Home")


@app.route("/decoded", methods=["GET", "POST"])
def decoded():
    sentence = session.get("sentence", "")
    
    # Handle empty sentence
    if not sentence or sentence.strip() == "":
        sentence = "No text was extracted from the image. Please try uploading a clearer image with readable text."
    
    print(f"Sentence from session: '{sentence}'")  # Debug print
    
    # Detect language only if we have valid text
    if sentence and len(sentence.strip()) > 3 and "Error" not in sentence:
        try:
            lang, conf = utils.detect_language(sentence)
            print(f"Language detection result: {lang}, confidence: {conf}")
        except Exception as e:
            print(f"Language detection failed: {e}")
            lang, conf = 'en', 0.0
    else:
        lang, conf = 'en', 0.0
    
    form = QRCodeData() 

    if request.method == "POST":
        try:
            generated_audio_filename = secrets.token_hex(10) + ".mp3"
            text_data = form.data_field.data
            translate_to = form.language.data
            
            print(f"Form data - Text: '{text_data}', Target lang: '{translate_to}'")
            
            # Validate form data
            if not text_data or text_data.strip() == "":
                form.data_field.errors.append("Please enter some text to convert to audio")
                return render_template("decoded.html", 
                                title="Decoded", 
                                form=form, 
                                lang=utils.languages.get(lang, 'english'),
                                audio=False
                            )

            # Translate text
            try:
                translated_text = utils.translate_text(text_data, translate_to)
                print(f"Translation result: '{translated_text}'")
            except Exception as e:
                print(f"Translation error: {e}")
                translated_text = text_data  # Use original text if translation fails
            
            # Generate audio
            try:
                from gtts import gTTS
                tts = gTTS(translated_text, lang=translate_to)
                
                file_location = os.path.join(
                                    app.config['AUDIO_FILE_UPLOAD'], 
                                    generated_audio_filename
                                )
                
                # Save file as audio
                tts.save(file_location)
                print(f"Audio saved to: {file_location}")
                
                # Update form with translated text
                form.data_field.data = translated_text

                return render_template("decoded.html", 
                                title="Decoded", 
                                form=form, 
                                lang=utils.languages.get(lang, 'english'),
                                audio=True,
                                file=generated_audio_filename
                            )
                            
            except Exception as e:
                print(f"TTS Error: {e}")
                form.data_field.errors.append(f"Audio generation failed: {str(e)}")
                
        except Exception as e:
            print(f"General error in decoded POST: {e}")
            import traceback
            print(f"Full traceback: {traceback.format_exc()}")
            form.data_field.errors.append(f"Processing failed: {str(e)}")

    # Set form data to extracted sentence
    form.data_field.data = sentence

    # Clear the sentence from session after use
    session["sentence"] = ""

    return render_template("decoded.html", 
                            title="Decoded", 
                            form=form, 
                            lang=utils.languages.get(lang, 'english'),
                            audio=False
                        )


@app.route("/audio_download/<filename>")
def audio_download(filename):
    """Download generated audio file"""
    audio_path = os.path.join(app.config['AUDIO_FILE_UPLOAD'], filename)
    
    if os.path.exists(audio_path):
        return send_file(audio_path, as_attachment=True)
    else:
        return redirect(url_for('index'))


@app.route("/clear_session")
def clear_session():
    """Clear all session data"""
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500