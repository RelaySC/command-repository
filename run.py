from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commandName = db.Column(db.String(20), unique=True)
    helpText = db.Column(db.String())
    response = db.Column(db.String())

    def __init__(self, commandName, helpText, response):
        self.commandName = commandName
        self.helpText = helpText
        self.response = response

    def __repr__(self):
        return '<Command %r>' % self.commandName

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()