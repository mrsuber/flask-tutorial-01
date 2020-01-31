from flask import Flask
app = Flask(__name__)
from app.views import mod as flask_welcome_mod
