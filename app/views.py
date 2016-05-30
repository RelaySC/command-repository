from flask import (
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    flash
)
from .models import Command
from .forms import CommandForm
from . import app, db

@app.route('/', methods=['POST', 'GET'])
def index():
    form = CommandForm()
    if form.validate_on_submit():
        command_name = request.form['command_name']
        if command_name.startswith('!'):
            command_name = command_name[1:]

        new_command = Command(command_name.lower(),
                              request.form['help_text'],
                              request.form['response'])
        db.session.add(new_command)
        db.session.commit()
        flash('Success! Your command has been added!', 'success')
        return redirect(url_for('index'))
    
    commands = Command.query.all()
    return render_template('index.html', commands=commands, form=form)


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