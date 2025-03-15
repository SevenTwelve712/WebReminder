from flask import Flask, render_template
from webreminder_app.pages.libraries import json_F

app = Flask(__name__)


@app.route('/')
def main():
    return '<p>Hello, this is main page</p>'


@app.route('/libraries/json')
def json():
    return json_F.page.render()
