import time
from flask import Flask

app = Flask('simpleServer')

@app.route('/')
def index():
    return time.ctime()

app.run(debug=True, port=3000, host='0.0.0.0')