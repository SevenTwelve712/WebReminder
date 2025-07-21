from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from webreminder_app.utils.content_table import *

commands = ContentTable(
    False,
    ['Команда', "Что делает"],
    [
        ContentTableLine(
            [
                'search',
                'Ищет пакеты с указанным файлом'
            ]
        ),
        ContentTableLine(
            [
                'find',
                'То же самое, что и search'
            ]
        ),
        ContentTableLine(
            [
                'list',
                'Список файлов пакета'
            ]
        ),
        ContentTableLine(
            [
                'show',
                'То же самое, что и list'
            ]
        )
    ]
)

options = ContentTable(
    False,
    ['Опция', "Что делает"],
    [
        ContentTableLine(
            [
                '-D',
                'Использует заданный пакет .deb как pattern, удобен для поиска конфликтов. Подразумевает -F'
            ]
        ),
        ContentTableLine(
            [
                '-f',
                'Позволяет читать шаблоны из файла. Если файл не задан, читает из stdin'
            ]
        ),
        ContentTableLine(
            [
                '-F',
                'Определяет заданные patterns как строку без регулярных выражений'
            ]
        ),
        ContentTableLine(
            [
                '-i',
                'Игнорирует case при поиске шаблонов'
            ]
        ),
        ContentTableLine(
            [
                '-l',
                'Выводит только имя пакета'
            ]
        ),
        ContentTableLine(
            [
                '-v',
                'Запускает режим отладки'
            ]
        ),
        ContentTableLine(
            [
                '-x',
                'Определяет заданные patterns как регулярные perl-выражения'
            ]
        ),
        ContentTableLine(
            [
                '-h',
                'Выводит справочное окно'
            ]
        )
    ]
)

kwargs = {
    'commands': commands,
    'options': options
}
html_path = 'linux/packages/apt-file.html'
page = Instruction('apt-file', html_path, kwargs, define_from_html(html_path))
