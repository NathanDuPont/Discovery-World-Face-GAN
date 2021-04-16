from flask import Flask
from flask import request

app = Flask(__name__)

# Configuration
# Add an environment variable as described below:
# FLASK_APP = server.py
# Powershell: $env:FLASK_APP = "server.py"
# Cmd: set FLASK_APP=server.py
# Bash/Linux: export FLASK_APP=server.py

url_for('static', filename='index.html')
url_for('static', filename='style.css')
url_for('static', filename='app.js')

@app.route('/')
def hello_world():
    return "Test"

@app.route('/processImage', method='POST')
def processImage():
    err = None
    
    imageBase64 = request.form['img']