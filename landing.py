import time
from flask import Flask, send_file

app = Flask('landing')


@app.route('/')
def index():
    return send_file('landing.html')


@app.route('/images/<filename>')
def get_image(file_name):
    return send_file('images/' + file_name)


app.run(debug=True, port=3000, host='0.0.0.0')