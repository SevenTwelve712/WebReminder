from webreminder_app.utils.content_table import *
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.unordered_list import UnorderedList

content = ContentTable(
    False,
    ['Атрибут', 'За что отвечает', 'Фиксированные значения'],
    [
        ContentTableLine(
            [
                'class',
                'Позволяет задать тегу стили или скрипты',
                ''
            ]
        ),
        ContentTableLine(
            [
                'dir',
                'Задает направление текста в элементе',
                str(UnorderedList(['ltr (left to right)', 'rtl (right to left)', 'auto']))
            ]
        ),
        ContentTableLine(
            [
                'id',
                'Предоставляет id элемента, чтобы его можно было идентифицировать при помощи css или js',
                ''
            ]
        ),
        ContentTableLine(
            [
                'style',
                'Позволяет прописывать стили css внутри тега',
                ''
            ]
        ),
        ContentTableLine(
            [
                'title',
                'Содержит инфо, отображающееся во всплывающей подсказке',
                ''
            ]
        )
    ]
)


instruction = Instruction(
    'Attributes',
    'attributes.html',
    {'content': content},
    {}
)
