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


def save_command(form):
    command_name = form['command_name']
    if command_name.startswith('!'):
        command_name = command_name[1:]

    new_command = Command(command_name.lower(),
                          form['help_text'],
                          form['response'])
    db.session.add(new_command)
    db.session.commit()


@app.route('/', methods=['POST', 'GET'])
def index():
    form = CommandForm()
    # validate_on_submit already checks request method but this allows us to enter a error message.
    if request.method == 'POST':
        if form.validate_on_submit():  # Checks WTForms validation.
            try:
                save_command(request.form)
                flash('Success! Your command has been added!',
                      'success')
            except Exception:
                flash('Oops! We couldn\'t add your command, double-check that name isn\'t already used.',
                      'error')
            finally:
                return redirect(url_for('index'))  
        else:
            flash('Oops! We couldn\'t add your command, double-check that name isn\'t already used.',
                  'error')
    
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


@app.route('/delete/<int:command_id>', methods=['GET'])
def delete_command(command_id):
    command = Command.query.filter_by(id=command_id).first()
    
    if not command:
        flash('Hmm... we couldn\'t find the command you were trying to remove.', 'error')
        return redirect(url_for('index'))
    
    try:
        db.session.delete(command)
        db.session.commit()
        flash('And another command bites the dust...', 'success')
    except:
        flash('We ran into an error when deleting this.', 'error')
    finally:
        return redirect(url_for('index')) 