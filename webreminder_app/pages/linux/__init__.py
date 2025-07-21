from flask import render_template

from webreminder_app import app, navbar
from webreminder_app.pages.linux.packages.apt import apt_F, apt_file_F


@app.route('/linux/packages/apt/apt')
def apt():
    return render_template('utils/instruction.html', instruction=apt_F.page, navbar=navbar, **apt_F.kwargs)


@app.route('/linux/packages/apt/apt-file')
def apt_file():
    return render_template('utils/instruction.html', instruction=apt_file_F.page, navbar=navbar, **apt_file_F.kwargs)