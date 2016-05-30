import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = os.environ.get('COMMAND_REPO_SECRET_KEY')

db = SQLAlchemy(app)

from . import models, views, commands