from webreminder_app.utils.content_table import *
from webreminder_app.utils.libraries_render import LibraryPage
from webreminder_app.utils.unordered_list import UnorderedList

content = ContentTable(
    'math',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine(
            [
                'ceil',
                'x',
                'Округление до ближайшего целого',
                'ceil(1.5)<hr>2'
            ]
        ),
        ContentTableLine(
            [
                'factorial',
                'x',
                'Возвращает факториал х',
                'factorial(10)<hr>3628800'
            ]
        ),
        ContentTableLine(
            [
                'frexp',
                'x',
                'Возвращает мантиссу и экпоненту числа (мантисса * 2 ** экспонента == х)',
                'frexp(103453222)<hr>(0.7707865685224533, 27)'
            ]
        ),
        ContentTableLine(
            [
                'ldexp',
                str(UnorderedList(['x', 'i'])),
                'Функция, обратная frexp. Возвращает x * 2 ** i',
                'ldexp(0.7707865685224533, 27)<hr>103453222'
            ]
        ),
        ContentTableLine(
            [
                'fsum',
                'iterable',
                'Тоже самое, что и sum, но для чисел с плавающей точкой точнее',
                'fsum([1, 2, 3])<hr>6.0'
            ]
        ),
        ContentTableLine(
            [
                'exp',
                'x',
                'exp ** x',
                'exp(5)<hr>148.4131591025766'
            ]
        ),
        ContentTableLine(
            [
                'pi',
                'Нет',
                'Выдает значение пи',
                'pi<hr>3.141592653589793'
            ]
        ),
        ContentTableLine(
            [
                'e',
                'Нет',
                'Выдает значение e',
                'e<hr>2.718281828459045'
            ]
        ),
        ContentTableLine(
            [
                'log',
                str(UnorderedList(['x', 'base'])),
                'Логарифм х по основанию base. Если base не задан, вычисляется натуральный логарифм',
                'log(27, 3)<hr>3.0'
            ]
        ),
        ContentTableLine(
            [
                'pow',
                str(UnorderedList(['x', 'y'])),
                'x ** y',
                'pow(5, 4)<hr>625.0'
            ]
        ),
        ContentTableLine(
            [
                'sqrt',
                'x',
                'Квадратный корень из x',
                'sqrt(36)<hr>6.0'
            ]
        ),
        ContentTableLine(
            [
                'cos',
                'x (в радианах)',
                'Вычисляет cos x',
                'cos(3.1415)<hr>0.9999999957076562'
            ]
        ),
        ContentTableLine(
            [
                'sin',
                'x (в радианах)',
                'Вычисляет sin x',
                'sin(1)<hr>0.8414709848078965'
            ]
        ),
        ContentTableLine(
            [
                'tan',
                'x (в радианах)',
                'Вычисляет tan x',
                'tan(1)<hr>1.5574077246549023'
            ]
        ),
        ContentTableLine(
            [
                'hypot',
                str(UnorderedList(['x', 'y'])),
                'Вычислет гипотенузу прямоугольного треугольника с катетами x и y',
                'hypot(3, 4)<hr>5.0'
            ]
        ),
        ContentTableLine(
            [
                'degrees',
                'x',
                'Переводит радианы в градусы',
                'degrees(1)<hr>57.29577951308232'
            ]
        ),
        ContentTableLine(
            [
                'radians',
                'x',
                'Переводит градусы в радианы',
                'radians(57.29577951308232)<hr>1.0'
            ]
        )
    ]
)

page = LibraryPage('math', False, content)
