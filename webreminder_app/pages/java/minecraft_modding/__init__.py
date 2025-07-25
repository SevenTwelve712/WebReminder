from flask import render_template

from webreminder_app import app, navbar
from webreminder_app.pages.java.minecraft_modding import entry_point_F, item_F, object_registering_F


@app.route('/java/minecraft_modding/entry_point')
def minecraft_entry_point():
    return render_template('utils/instruction.html', instruction=entry_point_F.instruction, navbar=navbar, **entry_point_F.kwargs)


@app.route('/java/minecraft_modding/item')
def minecraft_add_item():
    return render_template('utils/instruction.html', instruction=item_F.instruction, navbar=navbar, **item_F.kwargs)


@app.route('/java/minecraft_modding/object_registering')
def minecraft_object_registering():
    return render_template('utils/instruction.html', instruction=object_registering_F.instruction, navbar=navbar, **object_registering_F.kwargs)
