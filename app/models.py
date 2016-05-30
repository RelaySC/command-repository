from datetime import datetime
from . import db

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command_name = db.Column(db.String(20), unique=True)
    help_text = db.Column(db.String(), nullable=False)
    response = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(), nullable=False)

    def __init__(self, command_name, help_text, response):
        self.command_name = command_name
        self.help_text = help_text
        self.response = response
        self.date_added = datetime.now()

    def __repr__(self):
        return '<Command %r>' % self.command_name