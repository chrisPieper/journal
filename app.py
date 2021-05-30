from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mongoengine import MongoEngine
from wtforms.validators import DataRequired

from event import EventForm
from dateevents import DateEventsForm
from results import ResultsForm

app = Flask(__name__)
# app.config.from_pyfile('the-config.cfg')
app.config['SECRET_KEY'] = 'around the bend'
app.config['MONGODB_SETTINGS'] = {
    'db': 'journal_database',
    'host': 'localhost',
    'port': 27017
}

bootstrap = Bootstrap(app)
moment = Moment(app)
db = MongoEngine()
db.init_app(app)


# Data model
class Journal(db.Document):
    date = db.StringField()
    type = db.StringField()
    text = db.StringField()
    def to_json(self):
        return {"date": self.date,
                "type": self.type,
                "text": self.text}


# Error handlers
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
        return redirect(url_for('result'))
    return render_template('change.html', form=form, text=session.get('text'))


@app.route('/result', methods=['GET', 'POST'])
def result():
    date = request.args.get('date')
    journal = Journal.objects()
    print(journal[0].to_json())
    print(journal[1].to_json())
    table = ResultsForm()
    return render_template('results.html', table=table, name=session.get('name'))


# Delete data


# Find data
