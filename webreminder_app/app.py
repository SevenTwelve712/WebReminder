from flask import Flask, render_template, url_for
from webreminder_app.pages.libraries import json_F
from webreminder_app import navbar

app = Flask(__name__)


@app.route('/')
def main():
    return '<p>Hello, this is main page</p>'


@app.route('/libraries/json')
def json():
    return render_template('utils/library.html', library=json_F.page, navbar=navbar)
