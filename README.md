# journal

**Start virtual environment**
`$ source venv/bin/activate`

**Leaving virtual environment**
`$ deactivate`

**Installing packages**
`python3 -m pip install <package>`
`python3 -m pip install <package>==<version>`

**Upgrading packages**
`python3 -m pip install --upgrade <package>`

**Using requirements.txt file**
`python3 -m pip install -r requirements.txt`
`python3 -m pip freeze > requirements.txt`

**Starting flask code**
`$ export FLASK_APP=journal`
`$ export FLASK_ENV=development`
`$ export FLASK_RUN_PORT=8000`
`$ flask run`
