# app.py
import os, flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)


