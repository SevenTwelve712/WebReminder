from webreminder_app.utils.navigation_bar import *

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
            NavElem('jinja2', 'jinja_lib'),
            NavElem("python-docx", "python_docx")
        ]),
        NavHeaderBlock(NavElem('Инструкции', False), [
            NavElem('telebot'),
            NavElem('Шпаргалка по css', 'css_reminder'),
            NavElem('Шпаргалка по html', 'html_reminder'),
            NavElem('Атрибуты html', 'attributes'),
            NavElem('jinja2', 'jinja_inst'),
        ]),

        NavHeaderBlock(NavElem('Java', False), [
            NavElem('Основные положения', 'java_main'),
            NavElem('Работа с переменными', 'java_variables'),
            NavElem('Условные выражения и циклы', 'java_cond_expr_loops'),
            NavElem('Основы ООП', 'java_oop'),
            NavElem('Хранение данных', 'java_data_storage'),
            NavElem('Исключения', 'java_exceptions'),
            NavElem('Потоки', 'java_streams'),
            NavElem('Документация', 'java_documentation')
        ]),

        NavHeaderBlock(NavElem('Linux', False), [
            NavElem('apt'),
            NavElem('apt-file', 'apt_file'),
        ]),

        NavHeaderBlock(NavElem('Работа с сетью', False), [
            NavElem('SSH', 'ssh'),
            NavElem('nginx'),
            NavElem('acme.sh', 'acme_sh')
        ]),

        NavHeaderBlock(NavElem('Работа с QT', False), [
            NavElem('Основные положения', 'qt_main'),
            NavElem('Расположение элементов', 'qt_placement'),
            NavElem('Анимации', 'qt_animations'),
        ])
    ]
)
