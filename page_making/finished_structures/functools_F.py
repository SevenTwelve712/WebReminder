from page_making.classes.content_table import *
from page_making.classes.libraries_render import LibraryPage
from page_making.classes.unordered_list import UnorderedList
from pathlib import Path
from help.support.abspaths import static_pages

content = ContentTable(
    'functools',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [ContentTableLine(
        [
            '@total_ordering',
            'Нету',
            'Определяет методы сравнения в классах. Нужно определить только __eq__() и __lt__(), __le__(), __gt__(), или __ge__()',
            'Хуй я тут чо придумаю'
        ]
    ),
        ContentTableLine(
         [
             'reduce',
             str(UnorderedList(['function', 'iterable', 'start'])),
             'Берет первые два элемента, применяет к ним функцию, потом берет значение и третий элемент, применяет функцию и.т.д. Если задан start, то он берется как начальное значение',
             'reduce(lambda x, y: x + y, [2, 3, 4, 5], 1)<hr>15'
         ]
        ),
        ContentTableLine(
            [
                '@lru_cache',
                str(UnorderedList(['maxsize', 'typed'])),
                'Кэширует результаты вызова функции. Особенно полезен в рекурсивных функциях. maxsize определяет максимальный размер кэша (вроде в битах, но не уверен). typed определяет, как хранить различные типы. f(3) != f(3.0) при typed == True, иначе наоборот',
                'Стандартный синтаксис декоратора'
            ]
        )
     ]
)

page = LibraryPage('functools', False, content)
page.make_static(Path(static_pages, 'functools.html'))
