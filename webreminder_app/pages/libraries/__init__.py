from flask import render_template

from webreminder_app import app, navbar
from webreminder_app.pages.libraries import json_F, builtins_F, random_F, functools_F, itertools_F, csv_F, jinja_lib_F, \
    math_F, os_F


@app.route('/libraries/json')
def json():
    return render_template('utils/library.html', library=json_F.page, navbar=navbar)


@app.route('/libraries/builtins')
def builtins():
    return render_template('/utils/library.html', library=builtins_F.page, navbar=navbar)


@app.route('/libraries/random')
def random():
    return render_template('utils/library.html', library=random_F.page, navbar=navbar)


@app.route('/libraries/functools')
def functools():
    return render_template('utils/library.html', library=functools_F.page, navbar=navbar)


@app.route('/libraries/itertools')
def itertools():
    return render_template('utils/library.html', library=itertools_F.page, navbar=navbar)


@app.route('/libraries/csv')
def csv():
    return render_template('utils/library.html', library=csv_F.page, navbar=navbar)


@app.route('/libraries/jinja')
def jinja_lib():
    return render_template('utils/library.html', library=jinja_lib_F.page, navbar=navbar)


@app.route('/libraries/math')
def math():
    return render_template('utils/library.html', library=math_F.page, navbar=navbar)


@app.route('/libraries/os')
def os():
    return render_template('utils/library.html', library=os_F.page, navbar=navbar)