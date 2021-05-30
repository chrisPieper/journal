from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DateEventsForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    type = StringField('Type')
    description = TextAreaField('Description', validators=[DataRequired()])
