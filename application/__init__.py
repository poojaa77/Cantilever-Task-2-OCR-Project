from flask import Flask
import os
from flask_dropzone import Dropzone
from flask_session import Session

app = Flask(__name__)

# Secret key (use env var in production)
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    "dev-secret-key"  # fallback for local dev
)

# Session config
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Directory paths
dir_path = os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, 'static/uploaded_files/'),
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    AUDIO_FILE_UPLOAD=os.path.join(dir_path, 'static/audio_files/'),
    DROPZONE_REDIRECT_VIEW='decoded'
)

# Ensure upload directories exist
os.makedirs(app.config['UPLOADED_PATH'], exist_ok=True)
os.makedirs(app.config['AUDIO_FILE_UPLOAD'], exist_ok=True)

# Init Dropzone
dropzone = Dropzone(app)

# Import routes last
from application import routes
