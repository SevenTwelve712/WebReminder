from webreminder_app.utils.content_table import *
from webreminder_app.utils.libraries_render import LibraryPage
from pathlib import Path
from help.support.abspaths import static_pages

extra = ContentTable(
    False,
    ['В функциях чтения csv файла:', 'В функциях записи scv файла'],
    [ContentTableLine(['data.csv:<br>|a, f|,b,c<br>1,2,3<br>4,5,6<br>data = open("data.csv"))',
                       'data = [["a", "f", "b", "c"], ["1", "2", "3"], ["4", "5", "6"]]'
                       '<br>data_dicts =[{"a, f": "1", "b": "2", "c": "3"}, {"a, f": "4", "b": "5", "c": "6"}]'
                       '<br>result = open("result.csv", "w")<br>result.csv — пустой csv файл'],
                      'usual'),
     ]
)

content = ContentTable(
    'CSV',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine(
            [
                'reader',
                '<ul><li>iterable</li><li>delimiter</li><li>quotechar</li>',
                'Возвращает итерируемый объект, в котором записаны списки строк из файла',
                "list(csv.reader(data, delimiter=',', quotechar='|'))<hr>[['a, f', 'b', 'c'], ['1', '2', '3'], ['4', '5', '6']]"
            ]
        ),
        ContentTableLine(
            [
                'writer',
                "<ul><li>csvfile</li><li>delimiter,</li><li>quotechar</li></ul>",
                'Возвращает объект write, который может записывать в csvfile данные',
                "csv.writer(result, delimiter=',', quotechar='|')<hr>Теперь к объекту можно применять его методы"
            ]
        )
    ]
)

page = LibraryPage('csv', extra, content)