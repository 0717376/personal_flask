from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
     