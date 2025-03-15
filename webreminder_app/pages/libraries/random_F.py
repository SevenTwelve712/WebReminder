from webreminder_app.utils.content_table import *
from webreminder_app.utils.libraries_render import LibraryPage
from webreminder_app.utils.unordered_list import UnorderedList
from pathlib import Path
from help.support.abspaths import static_pages

content = ContentTable(
    'random',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine(
            [
                'randrange',
                str(UnorderedList(['start', 'stop=None', 'step=1'])),
                'Возвращает случайное число из последовательности',
                'random.randrange(0, 10, 2)<hr>6'
            ]
        ),
        ContentTableLine(
            [
                'randint',
                str(UnorderedList(['a', 'b'])),
                'Случайное число, a <= n <= b',
                'random.randint(3, 9)<hr>4'
            ]
        ),
        ContentTableLine(
            [
                'choice',
                'list',
                'Случайный элемент непустой последовательности',
                'random.choice([1, 2, 3, 4])<hr>3'
            ]
        ),
        ContentTableLine(
            [
                'shuffle',
                'list',
                'Перемешивает list. Работает только для изменяемых объектов',
                'a = [1, 2, 3, 4, 5]<br>random.shuffle(a)<hr>a --> [1, 5, 2, 4, 3]'
            ]
        ),
        ContentTableLine(
            [
                'sample',
                str(UnorderedList(['sequence', 'k'])),
                'Возвращает список длиной k из sequence',
                'random.sample([1, 2, 3, 4, 5, 6], 3)<hr>[1, 5, 3]'
            ]
        ),
        ContentTableLine(
            [
                'random',
                'Нет',
                'Случайное число от одного до единицы',
                'random.random()<hr>0.8279041920259892'
            ]
        ),
        ContentTableLine(
            [
                'uniform',
                str(UnorderedList(['a', 'b'])),
                'Случайное число с плавающей точкой. a <= n <= b',
                'random.uniform(3, 9)<hr>3.4430435793796352'
            ]
        )
    ]
)

page = LibraryPage('random', False, content)
