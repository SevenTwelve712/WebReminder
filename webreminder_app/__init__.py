from webreminder_app.pages.libraries import json_F, builtins_F, csv_F, functools_F, itertools_F, jinja_lib_F, math_F, os_F, random_F
from webreminder_app.pages.instructions import telebot_F, css_reminder_F, html_reminder_F, attributes_F, jinja_F
from webreminder_app.pages.linux.packages.apt import apt_F, apt_file_F
from webreminder_app.pages.navigation_bar import navbar_f
from flask import Flask, render_template

from webreminder_app.pages.instructions import telebot_F, css_reminder_F, html_reminder_F, attributes_F, jinja_F
from webreminder_app.pages.libraries import json_F, builtins_F, csv_F, functools_F, itertools_F, jinja_lib_F, math_F, \
    os_F, random_F
from webreminder_app.pages.linux.packages.apt import apt_F
from webreminder_app.pages.net import ssh_F, nginx_F, acme_sh_F
from webreminder_app.pages.java import java_main_F, java_variables_F, java_cond_expr_loops_F
from webreminder_app.pages.navigation_bar import navbar_f
from webreminder_app.pages.qt import qt_main_F, qt_placement_F, qt_animations_F

app = Flask(__name__)
navbar = navbar_f


@app.route('/')
def main():
    return '<p>Hello, this is main page</p>'


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


@app.route('/linux/packages/apt/apt')
def apt():
    return render_template('utils/instruction.html', instruction=apt_F.page, navbar=navbar, **apt_F.kwargs)


@app.route('/linux/packages/apt/apt-file')
def apt_file():
    return render_template('utils/instruction.html', instruction=apt_file_F.page, navbar=navbar, **apt_file_F.kwargs)


@app.route('/net/ssh')
def ssh():
    return render_template('utils/instruction.html', instruction=ssh_F.page, navbar=navbar, **ssh_F.kwargs)


@app.route('/net/nginx')
def nginx():
    return render_template('utils/instruction.html', instruction=nginx_F.page, navbar=navbar, **nginx_F.kwargs)


@app.route('/net/acme.sh')
def acme_sh():
    return render_template('utils/instruction.html', instruction=acme_sh_F.page, navbar=navbar)


@app.route('/qt/main')
def qt_main():
    return render_template('utils/instruction.html', instruction=qt_main_F.instruction, navbar=navbar, **qt_main_F.kwargs)


@app.route('/qt/placement')
def qt_placement():
    return render_template('utils/instruction.html', instruction=qt_placement_F.instruction, navbar=navbar, **qt_placement_F.kwargs)


@app.route('/qt/animations')
def qt_animations():
    return render_template('utils/instruction.html', instruction=qt_animations_F.instruction, navbar=navbar, **qt_animations_F.kwargs)


@app.route('/java/main')
def java_main():
    return render_template('utils/instruction.html', instruction=java_main_F.instruction, navbar=navbar, **java_main_F.kwargs)

@app.route('/java/variables')
def java_variables():
    return render_template('utils/instruction.html', instruction=java_variables_F.instruction, navbar=navbar, **java_variables_F.kwargs)

@app.route('/java/cond_expr_loops')
def java_cond_expr_loops():
    return render_template('utils/instruction.html', instruction=java_cond_expr_loops_F.instruction, navbar=navbar, **java_cond_expr_loops_F.kwargs)
