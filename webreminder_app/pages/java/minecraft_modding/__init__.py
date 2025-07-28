from flask import render_template

from webreminder_app import app, navbar
from webreminder_app.pages.java.minecraft_modding import entry_point_F, item_F, object_registering_F, block_F, \
    food_properties_F


@app.route('/java/minecraft_modding/entry_point')
def minecraft_entry_point():
    return render_template('utils/instruction.html', instruction=entry_point_F.instruction, navbar=navbar, **entry_point_F.kwargs)


@app.route('/java/minecraft_modding/item')
def minecraft_add_item():
    return render_template('utils/instruction.html', instruction=item_F.instruction, navbar=navbar, **item_F.kwargs)


@app.route('/java/minecraft_modding/object_registering')
def minecraft_object_registering():
    return render_template('utils/instruction.html', instruction=object_registering_F.instruction, navbar=navbar, **object_registering_F.kwargs)


@app.route('/java/minecraft_modding/block')
def minecraft_block():
    return render_template('utils/instruction.html', instruction=block_F.instruction, navbar=navbar, **block_F.kwargs)


@app.route('/java/minecraft_modding/food_properties')
def minecraft_food_properties():
    return render_template('utils/table_only.html', page=food_properties_F.page, navbar=navbar)