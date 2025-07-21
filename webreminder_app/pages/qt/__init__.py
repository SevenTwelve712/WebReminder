from flask import render_template
from webreminder_app import app, navbar
from webreminder_app.pages.qt import main_F, placement_F, animations_F


@app.route('/qt/main')
def qt_main():
    return render_template('utils/instruction.html', instruction=main_F.instruction, navbar=navbar, **main_F.kwargs)


@app.route('/qt/placement')
def qt_placement():
    return render_template('utils/instruction.html', instruction=placement_F.instruction, navbar=navbar, **placement_F.kwargs)


@app.route('/qt/animations')
def qt_animations():
    return render_template('utils/instruction.html', instruction=animations_F.instruction, navbar=navbar, **animations_F.kwargs)