import pathlib, os
from flask import Flask
from dotenv import load_dotenv

app = Flask("my_app")
app.config['FOLDER'] = str(pathlib.Path(__file__).parent.absolute()).replace('\\', '/')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

load_dotenv(f"{app.config['FOLDER']}/.env")
app.secret_key = os.getenv("SECRET_KEY")



