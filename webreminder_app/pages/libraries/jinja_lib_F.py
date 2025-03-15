from webreminder_app.utils.content_table import *
from webreminder_app.utils.libraries_render import LibraryPage
from help.support.abspaths import static_pages
from pathlib import Path

content = ContentTable(
    'jinja2',
    ['Элемент библиотеки', 'Тип', 'Аргументы/Значения по дефолту', 'За что отвечает'],
    [
        ContentTableLine('environment', 'subhead'),
        ContentTableLine(
            [
                'Environment',
                'класс',
                'Дохуя всего, смотри ниже',
                'Задает основной объект jinja — среду, через нее будет осуществляться работа с шаблонами'
            ]
        ),
        ContentTableLine(
            [
                'env.loader',
                "переменная",
                'None',
                'Загрузчик шаблонов среды. Смотри ниже в таблице, какие бывают загрузчики. задает место, где среда ищет шаблоны'
            ]
        ),
        ContentTableLine(
            [
                'env.autoescape',
                "переменная",
                'True',
                'Позволяет задать правила экранирования. По дефолту True (весь html экранируется), можно как-то определять с помощью функции select_autoescape, но я так и не разобрался, как она работает'
            ]
        ),
        ContentTableLine(
            [
                'env.block_start_string',
                "переменная",
                '"{%"',
                'Задает символ начала блока'
            ]
        ),
        ContentTableLine(
            [
                'env.block_end_string',
                "переменная",
                '"%}"',
                'Задает символ конца блока'
            ]
        ),
        ContentTableLine(
            [
                'env.variable_start_string',
                "переменная",
                '"{{"',
                'задает символ начала переменной',
            ]
        ),
        ContentTableLine(
            [
                'env.variable_end_string',
                "переменная",
                '"}}"',
                'Задает символ конца переменной'
            ]
        ),
        ContentTableLine(
            [
                'env.comment_start_string',
                "переменная",
                '"{#"',
                'Задает символ начала комментария'
            ]
        ),
        ContentTableLine(
            [
                'env.comment_end_string',
                "переменная",
                '"#}',
                'Задает символ конца комментария'
            ]
        ),
        ContentTableLine(
            [
                'env.lstrip_blocks',
                "переменная",
                'False',
                'Вроде убирает незначащие пробелы/табуляции в начале строки'
            ]
        ),
        ContentTableLine(
            [
                'env.trim_blocks',
                "переменная",
                'False',
                'Вроде убирает строку после тега'
            ]
        ),
        ContentTableLine(
            [
                'env.get_template',
                'метод',
                'path',
                'Возвращает объект шаблона, находящегося по пути path'
            ]
        ),
        ContentTableLine('template', 'subhead'),
        ContentTableLine(
            [
                'templ.render',
                'метод',
                '*kwargs',
                'Рендерит шаблон, подставляя в качестве переменных kwargs. Важно, чтобы имена аргументов в шаблоне и в kwargs совпадали'
            ]
        ),
        ContentTableLine('loaders', 'subhead'),
        ContentTableLine(
            [
                'FileSystemLoader',
                'класс',
                'path',
                'Создает объект, который может быть использован в качестве загрузчика в env. Env сможет загружать любые шаблоны из файлвой директории path'
            ]
        ),
        ContentTableLine(
            [
                'Возможно тут будут еще загрузчики, но я другими пока не пользовался',
                '',
                '',
                ''
            ]
        )
    ]
)

page = LibraryPage(
    'jinja2',
    False, content
)
page.make_static(Path(static_pages, 'jinja2_lib.html'))
