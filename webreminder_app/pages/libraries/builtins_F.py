from webreminder_app.utils.content_table import *
from webreminder_app.utils.table_only import TableOnlyPage
from webreminder_app.utils.unordered_list import UnorderedList

content = ContentTable(
    'Встроенные функции',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine('Работа с файлами', type_='subhead'),
        ContentTableLine(
            [
                'print',
                str(UnorderedList(['values', 'sep=" "', 'end="\\n"', 'file=sys.stdout'])),
                'Записывает values через sep, (в конце записи ставит end) в file',
                "print('Филипп гей', 'А Глеб не гей', sep='/n'<hr>Филипп гей<br>А Глеб не гей"
            ]
        ),
        ContentTableLine(
            [
                'input',
                'Нет',
                'Записывает данные из стандартного ввода',
                "a = input()<br>4<hr>a -> '4'"
            ]
        ),
        ContentTableLine(
            [
                'open',
                str(UnorderedList(['file', 'mode="r"', 'encoding=None', 'newline=None'])),
                'Открывает файл в кодировке encoding и ретёрнит поток данных (можно идти фором). mode отвечает за режим открытия файла',
                "a = open('in.txt')<hr>a -> <_io.TextIOWrapper name='in.txt' mode='r' encoding='cp1251'>"
            ]
        ),
        ContentTableLine('Информация об объекте', 'subhead'),
        ContentTableLine(
            [
                'len',
                'object',
                'Выводит длину object',
                "len('12345')<hr>5"
            ]
        ),
        ContentTableLine(
            [
                'min',
                str(UnorderedList(['*args', 'key=None'])),
                'Выводит минимальное значение',
                "min('12345')<hr>'1'"
            ]
        ),
        ContentTableLine(
                    [
                        'max',
                        str(UnorderedList(['*args', 'key=None'])),
                        'Выводит максимальное значение',
                        "max('12345')<hr>'5'"
                    ]
                ),
        ContentTableLine(
            [
                'any',
                'iterable',
                'Возвращает True если хотя бы один элемент в iterable object True. Иначе False',
                'any([1, 2, 3, 4, 0, 0])<hr>True'
            ]
        ),
        ContentTableLine(
            [
                'all',
                'iterable',
                'Возвращает True если все элементы в iterable object True (или если iterable object пустой). Иначе False',
                'all([1, 2, 3, 4, 0, 0])<hr>False'
            ]
        ),
        ContentTableLine(
            [
                'dir',
                'object',
                'Если object не задан, то возвращает список всех локальных переменных, если object есть, то список всех атрибутов object',
                "dir([1, 2, 3, 4])<hr>['__add__', '__class__', ... 'remove', 'reverse', 'sort']"
            ]
        ),
        ContentTableLine(
            [
                'type',
                'object',
                'Возвращает тип object. Еще можно как-то сделать объект этого типа, но это ебля в сраку с другими аргументами',
                "type('12345')hr><class 'str'>"
            ]
        ),
        ContentTableLine(
            [
                'help',
                'object',
                'Выводит документацию объекта',
                'help(str)<hr>class str(object)<br>str(object='') -> str...'
            ]
        ),
        ContentTableLine(
            [
                'chr',
                'x',
                'Возвращает символ, соответствующий числу x в таблице Юникода',
                "chr(123)<hr>'{'"
            ]
        ),
        ContentTableLine(
            [
                'ord',
                'symbol',
                'Возвращает номер symbol в таблице юникода',
                "ord('h')<hr>104"
            ]
        ),
        ContentTableLine(
            [
                'round',
                str(UnorderedList(['number', 'ndifits=None'])),
                'Округляет number до ndigits знаков после запятой',
                'round(5.76543, 2)<hr>5.77'
            ]
        ),
        ContentTableLine(
            [
                'bin',
                'x',
                'Возвращает строку "0b{число в двоичной}"',
                "bin(45)<hr>'0b101101'"
            ]
        ),
        ContentTableLine(
            [
                'oct',
                'x',
                "Возвращает строку '0o{число в восьмеричной}'",
                "oct(45)<hr>'0o55'"
            ]
        ),
        ContentTableLine(
            [
                'hex',
                'x',
                "Возвращает строку '0x{число в шестнадцатиричной}'",
                "hex(45)<hr>'0x2d'"
            ]
        ),
        ContentTableLine('Итераторы', 'subhead'),
        ContentTableLine(
            [
                'enumerate',
                str(UnorderedList(['iterable', 'start=0'])),
                'Возвращает объект, в котором находятся кортежи (номер элемента + start, элемент)',
                'list(enumerate([1, 2, 3, 4, 5], start=1))<hr>[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]'
            ]
        ),
        ContentTableLine(
            [
                'zip',
                '*iterables',
                'Комбинирует элементы заданных списков по порядку в кортежи (все первые элементы в один кортеж, все вторые — в следующий итд)<hr>Прим: берутся элементы самого короткого iterable, все остальные игнорируются (см.пример)',
                "list(zip('abcdefg', range(3), range(4)))<hr>[('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]"
            ]
        ),
        ContentTableLine(
            [
                'reversed',
                'iterable',
                'Переворачивает iterable',
                "list(reversed('12345'))<hr>['5', '4', '3', '2', '1']"
            ]
        ),
        ContentTableLine(
            [
                'next',
                str(UnorderedList(['iterable', 'x'])),
                'Возвращает следующее значение iterable, если iterable закончился, то х',
                'a = iter([1, 2, 3])<br>next(a)<hr>1'
            ]
        ),
        ContentTableLine('Обработка объекта', 'subhead'),
        ContentTableLine(
            [
                'sorted',
                str(UnorderedList(['object', 'key=None', 'reverse=False'])),
                'Сортирует список по правилу key (key дб функцией). Если reverse is True, то сортировка идет по убыванию',
                "sorted([2, 8, 4, 1, 7, 3])<hr>[1, 2, 3, 4, 7, 8]"
            ]
        ),
        ContentTableLine(
            [
                'eval',
                'source',
                'Возвращает выполненный source (source — кусок кода в виде строки)',
                "eval('print(5 if 5 > 6 else 89)')<hr>89"
            ]
        ),
        ContentTableLine(
            [
                'filter',
                str(UnorderedList(['function=lambda x: True if x else False', 'iterable'])),
                'Возвращает итератор, в котором находится все элементы, удовлетворяющие function',
                "ist(filter(lambda x: True if x > 5 else False, [1, 3, 6, 9, 11, 2]))<hr>[6, 9, 11]"
            ]
        ),
        ContentTableLine(
            [
                'map',
                str(UnorderedList(['func', 'iterable'])),
                'Возвращает итератор, в котором находятся объекты из iterable, к которым применили function',
                "list(map(int, ['1', '2', '3', '4', '5']))<hr>[1, 2, 3, 4, 5]"
            ]
        ),
        ContentTableLine(
            [
                'int',
                str(UnorderedList(['x', 'base=10'])),
                'Переводит x из системы исчисления base в десятичную',
                "int('100010', base=2)<hr>34"
            ]
        ),
        ContentTableLine('Создание нового объекта', 'subhead'),
        ContentTableLine(
            [
                'range',
                str(UnorderedList(['start=0', 'stop', 'step=1'])),
                'Возвращает последовательность чисел от start до stop - 1 с шагом step',
                "list(range(1, 7, 2))<hr>[1, 3, 5]"
            ]
        )
    ]
)

page = TableOnlyPage(
    'builtins',
    False,
    content
)
