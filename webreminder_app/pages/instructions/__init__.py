from flask import render_template

from webreminder_app import navbar, app
from webreminder_app.pages.instructions import telebot_F, css_reminder_F, html_reminder_F, attributes_F, jinja_F


@app.route('/instructions')
def instructions():
    return render_template('utils/instructions.html', navbar=navbar)


@app.route('/instructions/telebot')
def telebot():
    return render_template('utils/instruction.html', instruction=telebot_F.instruction, navbar=navbar, **telebot_F.kwargs)


@app.route('/instructions/css_reminder')
def css_reminder():
    return render_template('utils/instruction.html', instruction=css_reminder_F.instruction, navbar=navbar, **css_reminder_F.kwargs)


@app.route('/instructions/html_reminder')
def html_reminder():
    return render_template('utils/instruction.html', instruction=html_reminder_F.instruction, navbar=navbar, **html_reminder_F.kwargs)


@app.route('/instructions/attributes')
def attributes():
    return render_template('utils/instruction.html', instruction=attributes_F.instruction, navbar=navbar, content=attributes_F.content)


@app.route('/instructions/jinja')
def jinja_inst():
    return render_template('utils/instruction.html', instruction=jinja_F.page, navbar=navbar, **jinja_F.kwargs)