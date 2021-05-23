from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# class DateEventsForm(FlaskForm):
#     date = DateField(id='datepick')

class DateEventsForm(FlaskForm):
    text = TextAreaField('Events', validators=[DataRequired()])
