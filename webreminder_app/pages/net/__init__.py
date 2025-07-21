from flask import render_template

from webreminder_app import app, navbar
from webreminder_app.pages.net import ssh_F, nginx_F, acme_sh_F


@app.route('/net/ssh')
def ssh():
    return render_template('utils/instruction.html', instruction=ssh_F.page, navbar=navbar, **ssh_F.kwargs)


@app.route('/net/nginx')
def nginx():
    return render_template('utils/instruction.html', instruction=nginx_F.page, navbar=navbar, **nginx_F.kwargs)


@app.route('/net/acme.sh')
def acme_sh():
    return render_template('utils/instruction.html', instruction=acme_sh_F.page, navbar=navbar)