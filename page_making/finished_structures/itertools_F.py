from page_making.classes.content_table import *
from page_making.classes.libraries_render import LibraryPage
from page_making.classes.unordered_list import UnorderedList
from pathlib import Path
from help.support.abspaths import static_pages

content = ContentTable(
    'itertools',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [ContentTableLine(
        ['cycle',
         'iterable',
         'Возвращает iterable бесконечное количество раз',
         'Не будет']
    ),
        ContentTableLine(
            ['accumulate',
             'iterable',
             'Выдает суммы всех элементов от 0 до i (см. пример)',
             'list(accumulate([1, 2, 3, 4]))<hr>[1, 3, 6, 10]'
             ]
        ),
        ContentTableLine(
            [
                'chain',
                '*iterables',
                'Возвращает элементы из iterables по очереди (сначала все из первого, потом все из второго итд)',
                'list(chain([1, 2, 3, 4], [5, 6, 7, 8]))<hr>[1, 2, 3, 4, 5, 6, 7, 8]'
            ]
        ),
        ContentTableLine(
            [
                'combinations',
                str(UnorderedList(['iterable', 'r'])),
                'Возвращает кортежи в которых записаны комбинации длиной r последовательно идущих элементов iterable без повторений',
                "list(combinations('1234', 2))<hr>[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]"
            ]
        ),
        ContentTableLine(
            [
                'combinations_witd_replacement',
                str(UnorderedList(['iterable', 'r'])),
                'То же самое, что и combinations, но элементы могут повторяться',
                "list(combinations_witd_replacement('1234', 2))<hr>[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('2', '2'), ('2', '3'), ('2', '4'), ('3', '3'), ('3', '4'), ('4', '4')]"
            ]
        ),
        ContentTableLine(
            [
                'compress',
                str(UnorderedList(['data', 'condition'])),
                'Возвращает data[i] если condition[i]',
                "list(compress('1234', [1, 0, 1, 0]))<hr>['1', '3']"
            ]
        ),
        ContentTableLine(
            [
                'zip_longest',
                str(UnorderedList(['*iterables', 'fillvalue=None'])),
                'То же самое, что и zip, но берется самый длинный iterable, а недостающие элементы из более коротких дополняются fillvalue',
                "list(zip_longest('1234', '12', fillvalue='A'))<hr>[('1', '1'), ('2', '2'), ('3', 'A'), ('4', 'A')]"
            ]
        ),
        ContentTableLine(
            [
                'groupby',
                str(UnorderedList(['iterable', 'key=None'])),
                'Группирует элементы по значению. Значение получается применением функции key к элементу (если аргумент key не указан, то значением является сам элемент)',
                "b = groupby([1, 2, 3, 4, 5, 6], key=lambda x: '>= 3' if x >= 3 else '< 3')<br>list(map(lambda x: (x[0], list(x[1])), b))<hr>[('< 3', [1, 2]), ('>= 3', [3, 4, 5, 6])]<hr>Примечание: list(b) -> [] после операции (хуй знает поч так)"
            ]
        ),
        ContentTableLine(
            [
                'permutations',
                str(UnorderedList(['iterable', 'r='])),
                'Возвращает перестановки любых неповторяющихся элементов длиной r',
                "list(permutations([1, 2, 3, 4], r=2))<hr>[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]"
            ]
        ),
        ContentTableLine(
            [
                'product',
                str(UnorderedList(['iterable', 'repeat='])),
                'Возвращает перестановки любых элементов длиной r',
                "list(product('123', repeat=2))<hr>[('1', '1'), ('1', '2'), ('1', '3'), ('2', '1'), ('2', '2'), ('2', '3'), ('3', '1'), ('3', '2'), ('3', '3')]"
            ]
        ),
    ]
)


page = LibraryPage('itertools', False, content)
page.make_static(Path(static_pages, 'itertools.html'))
