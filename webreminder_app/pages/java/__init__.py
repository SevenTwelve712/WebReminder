from webreminder_app import app, navbar

from flask import render_template

from webreminder_app.pages.java import main_F, variables_F, cond_expr_loops_F, oop_F, data_storage_F, exceptions_F, \
    streams_F, documentation_F


@app.route('/java/main')
def java_main():
    return render_template('utils/instruction.html', instruction=main_F.instruction, navbar=navbar, **main_F.kwargs)


@app.route('/java/variables')
def java_variables():
    return render_template('utils/instruction.html', instruction=variables_F.instruction, navbar=navbar, **variables_F.kwargs)


@app.route('/java/cond_expr_loops')
def java_cond_expr_loops():
    return render_template('utils/instruction.html', instruction=cond_expr_loops_F.instruction, navbar=navbar, **cond_expr_loops_F.kwargs)

@app.route('/java/oop')
def java_oop():
    return render_template('utils/instruction.html', instruction=oop_F.instruction, navbar=navbar, **oop_F.kwargs)


@app.route('/java/data_storage')
def java_data_storage():
    return render_template('utils/instruction.html', instruction=data_storage_F.instruction, navbar=navbar, **data_storage_F.kwargs)


@app.route('/java/exceptions')
def java_exceptions():
    return render_template('utils/instruction.html', instruction=exceptions_F.instruction, navbar=navbar, **exceptions_F.kwargs)


@app.route('/java/streams')
def java_streams():
    return render_template('utils/instruction.html', instruction=streams_F.instruction, navbar=navbar, **streams_F.kwargs)


@app.route('/java/documentation')
def java_documentation():
    return render_template('utils/instruction.html', instruction=documentation_F.instruction, navbar=navbar, **documentation_F.kwargs)