from core import db

# -- flask --
DEBUG = True
SECRET_KEY = "placeholder"
# SERVER_NAME = ""
IMG_EXT = ["jpg", "jpeg", "png", "gif"]
IMG_MIME = ["image/jpg", "image/jpeg", "image/png", "image/gif"]
MAX_CONTENT_LENGTH = 20000000

# -- flask-sqlalchemy --
DB_NAME = "data.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# -- flask-session --
SESSION_TYPE = "sqlalchemy"
SESSION_SQLALCHEMY = db