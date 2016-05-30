from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class CommandForm(Form):
    command_name = StringField(label='Command',
                               description='What command should the user run to get your response?',
                               validators=[DataRequired(), Length(min=1, max=20)])
    help_text = TextAreaField(label='Help Text',
                              description='What should be written next to the command in the `!help` listing?',
                              validators=[DataRequired()])
    response = TextAreaField(label='Response',
                             description='What should the bot respond with when the user has run the command?',
                             validators=[DataRequired()])