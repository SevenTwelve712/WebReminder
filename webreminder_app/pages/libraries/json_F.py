from webreminder_app.utils.content_table import *
from webreminder_app.utils.table_only import TableOnlyPage
from webreminder_app.utils.unordered_list import UnorderedList

extra = ContentTable(
    False,
    ['В функциях чтения json файла', 'В функциях записи json файла'],
    [ContentTableLine(
        [
            'data.json:<br>{"1": ["a", "b", "c"], "2": ["а", "б", "в"]}<br>data = open("data.json", encoding="utf8")',
            "data = {1: ['a', 'b', 'c'], 2: ['а', 'б', 'в']}<br>result = open('result.json', 'w', encoding='utf8')<br>result.json — пустой json файл"
        ],
        'usual')]
)

content = ContentTable(
    'json',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine(
            [
                'dump',
                str(UnorderedList(['data', 'result file', 'indent', 'ensure_ascii=True'])),
                'Загружает данные из data в result file в формате json. indent отвечает за визуальный отступ строк в json файле, ensure_ascii отвечает за кодировку',
                'json.dump(data, result_file, ensure_ascii=False)<hr>result_file.json:<br>{"1": ["a", "b", "c"], "2": ["а", "б", "в"]}'
            ]
        ),
        ContentTableLine(
            [
                'load',
                'file',
                'Возвращает питоновский объект из file',
                "print(json.load(data))<hr>{'1': ['a', 'b', 'c'], '2': ['а', 'б', 'в']}"
            ]
        )
    ]
)

page = TableOnlyPage('json', extra, content)
