from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)
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


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        command_name = request.form['command_name']
        if command_name.startswith('!'):
            command_name = command_name[1:]

        new_command = Command(command_name,
                              request.form['help_text'],
                              request.form['response'])
        db.session.add(new_command)
        db.session.commit()
        return redirect(url_for('index'))
    
    commands = Command.query.all()
    return render_template('index.html', commands=commands)

@app.route('/json', methods=['GET'])
def json():
    commands = Command.query.all()
    return jsonify([{
        "command": command.command_name,
        "description": command.help_text,
        "response": command.response,
        "hidden": False
    } for command in commands])

@app.route('/<int:command_id>', methods=['DELETE'])
def modify_command(command_id):
    if request.method == 'DELETE':
        command = Command.query.filter_by(id=command_id).first()
        db.session.delete(command)
        db.session.commit()
        return 'OK';

    return 'ERROR';
    

@app.cli.command()
def create_database():
    db.create_all()