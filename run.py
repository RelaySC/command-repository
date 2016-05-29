from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command_name = db.Column(db.String(20), unique=True)
    help_text = db.Column(db.String())
    response = db.Column(db.String())

    def __init__(self, command_name, help_text, response):
        self.command_name = command_name
        self.help_text = help_text
        self.response = response

    def __repr__(self):
        return '<Command %r>' % self.command_name


@app.route("/")
def index():
    commands = Command.query.all()
    return render_template('index.html', commands=commands)

if __name__ == "__main__":
    app.run()