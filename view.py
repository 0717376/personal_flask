from app import app
from flask import render_template


@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sayname')
def sayname():
    return '<h1>Hello Flask</h1>'
