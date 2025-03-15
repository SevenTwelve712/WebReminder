from webreminder_app.utils.navigation_bar import *
from os.path import abspath
from help.support.abspaths import static_pages


navbar_f = NavigationBar(
    [
        NavHeaderBlock(NavElem('Главная', False), False),
        NavHeaderBlock(NavElem('Библиотеки', False), [
            NavElem('builtins'),
            NavElem('csv'),
            NavElem('functools'),
            NavElem('itertools'),
            NavElem('json'),
            NavElem('math'),
            NavElem('os'),
            NavElem('random'),
            NavElem('jinja2')
        ]),
        NavHeaderBlock(NavElem('Инструкции', False), [
            NavElem('telebot'),
            NavElem('css_reminder'),
            NavElem('html_reminder'),
            NavElem('attributes'),
            NavElem('jinja2')
        ])
    ]
)
# TODO: дописать navbar
