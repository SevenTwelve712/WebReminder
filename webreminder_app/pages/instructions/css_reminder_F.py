from webreminder_app.utils.chapter_list import define_from_html
from webreminder_app.utils.content_table import *
from webreminder_app.utils.instruction import Instruction

useful = ContentTable(
    False,
    ['Свойства', 'За что отвечают'],
    [
        ContentTableLine(
            [
                'margin, margin-[top, bottom, left, right]',
                'Задает отступ от границы элемента до границы родительского элемента'
            ]
        ),
        ContentTableLine(
            [
                'padding, padding-[top, bottom, left, right]',
                'Задает отступ от границы элемента до его содержимого'
            ]
        ),
        ContentTableLine(
            [
                'font-family',
                'Задает шрифт'
            ]
        ),
        ContentTableLine(
            [
                'font-size, font-color', 'Задает размер и цвет шрифта'
            ]
        ),
        ContentTableLine(
            [
                'width, height',
                'Устанавливает ширину и высоту элемента (можно указывать как в пикселях, так и в процентах)'
            ]
        ),
        ContentTableLine(
            [
                'background',
                'Задает цвет задника'
            ]
        ),
        ContentTableLine(
            [
                'border',
                'Позволяет задать границу вокруг элемента (это универсальное свойство, можно сразу определить бордер, например, border: 3px solid red; задаст черную сплошную границу в 3 пикселя'
            ]
        ),
        ContentTableLine(
            [
                'border-[color, width, style, radius]',
                'Позволяет задать цвет, ширину, стиль и радиус бордера (так же можно конкретизировать границы с определенной стороны, например, border-bottom-style)'
            ]
        ),
        ContentTableLine(
            [
                'float',
                'Определяет, по какой стороне выравнивается элемент и как его обтекают другие элементы'
            ]
        ),
        ContentTableLine(
            [
                '[max, min]-[width-height]',
                'Устанавливает масксимальную и минимальную ширину и высоту элемента'
            ]
        )
    ]
)

css_info = """селектор {
	свойство: значение
}"""

tag = """h2 {
	font-family: "for_captions";
	font-size: 35px;
}"""

class_ = """.my_class{
	border: 3px solid black;
}"""

html_placement = 'instructions/css_reminder.html'
headers = define_from_html(html_placement)

kwargs = {
    'useful': useful,
    'css_info': css_info,
    'tag': tag,
    'class': class_
}

instruction = Instruction(
    'Css reminder',
    html_placement,
    kwargs,
    headers
)
