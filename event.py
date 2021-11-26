from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    type = StringField('Type', validators=[])
    text = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

