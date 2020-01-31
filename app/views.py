from flask import render_template,Blueprint
from app import app
mod = Blueprint('transaction', __name__, url_prefix='/api/v1')


@app.route('/')
@app.route('/index')
def index():
    first_variable = "Hello World"
    title = "Welcome to Flask"
    return render_template('index.html', title='Home', first_variable=first_variable)
