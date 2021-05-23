from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms.validators import DataRequired

from event import EventForm
from dateevents import DateEventsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'around the bend'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# View data
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DateEventsForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


# Create/Edit data
@app.route('/change', methods=['GET', 'POST'])
def change():
    form = EventForm()
    if form.validate_on_submit():
        # text = session.get('text')
        form.text.data
        form.date.data
        form.type.data
        session['text'] = form.text.data
        return redirect(url_for('index'))
    return render_template('change.html', form=form, text=session.get('text'))


# Delete data


# Find data
