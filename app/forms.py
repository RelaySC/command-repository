from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class CommandForm(Form):
    command_name = StringField(label='Command',
                               description='What command will the user run?',
                               validators=[DataRequired(), Length(min=1, max=20)])
    help_text = TextAreaField(label='Help Text',
                              description='What does your command do?',
                              validators=[DataRequired()])
    response = TextAreaField(label='Response',
                             description='What should the bot say back?',
                             validators=[DataRequired()])