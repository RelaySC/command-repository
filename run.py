from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command_name = db.Column(db.String(20), unique=True)
    help_text = db.Column(db.String(), nullable=False)
    response = db.Column(db.String(), nullable=False)

    def __init__(self, command_name, help_text, response):
        self.command_name = command_name
        self.help_text = help_text
        self.response = response

    def __repr__(self):
        return '<Command %r>' % self.command_name


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        new_command = Command(request.form['command_name'],
                              request.form['help_text'],
                              request.form['response'])
        db.session.add(new_command)
        db.session.commit()
    
    commands = Command.query.all()
    return render_template('index.html', commands=commands)

if __name__ == "__main__":
    app.run()