from flask_table import table, Col

class ResultsForm():
    id = Col('id', show=False)
    date = Col('date')
    description = Col('description')
    type = Col('type')