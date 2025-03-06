from page_making.classes.navigation_bar import *
from os.path import abspath
from help.support.abspaths import static_pages


navbar_f = NavigationBar(
    [
        NavHeaderBlock(NavElem('Главная', False), False),
        NavHeaderBlock(NavElem('Библиотеки', False), [
            NavElem('csv', abspath(f'{static_pages}/csv.html')),
            NavElem('functools', abspath(f'{static_pages}/functools.html')),
            NavElem('itertools', abspath(f'{static_pages}/itertools.html')),
            NavElem('json', abspath(f'{static_pages}/json.html')),
            NavElem('math', abspath(f'{static_pages}/math.html')),
            NavElem('os', abspath(f'{static_pages}/os.html')),
            NavElem('random', abspath(f'{static_pages}/random.html')),
        ]),
        NavHeaderBlock(NavElem('Инструкции', False), [
            NavElem('telebot', static_pages + '/telebot.html')
        ])
    ]
)
# TODO: дописать navbar
