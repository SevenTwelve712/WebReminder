from flask import render_template
from webreminder_app import app, navbar
from webreminder_app.pages.vagray import vagray_start


@app.route('/vagray/start')
def vagray_start_page():
    return render_template('utils/instruction.html', instruction=vagray_start.instruction, navbar=navbar, **vagray_start.kwargs)
