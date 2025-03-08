from page_making.classes.content_table import ContentTable, ContentTableLine
from page_making.classes.unordered_list import UnorderedList
from page_making.classes.instruction import Instruction
from pathlib import Path
from help.support.abspaths import static_pages, jinja_templs
from help.support.escape import escape
from page_making.classes.chapter_list import define_from_html

div_table = ContentTable(
    False,
    ['Атрибут тега', 'За что отвечает'],
    [
        ContentTableLine(
            [
                'align',
                'Задает выравнивание содержимого коробки'
            ]
        ),
        ContentTableLine(
            [
                'title',
                'Задает всплывающую подсказку'
            ]
        )
    ]
)

table_attr = ContentTable(
    False,
    ['Атрибут тега', 'За что отвечает'],
    [
        ContentTableLine(
            [
                'align',
                'Задает выравнивание содержимого таблицы'
            ]
        ),
        ContentTableLine(
            [
                'все остальное',
                'Там еще дохера всего, но это я бы уже прописывал в css'
            ]
        )
    ]
)

table_tags = ContentTable(
    False,
    ['Тег', 'Значение в иерархии таблицы'],
    [
        ContentTableLine(
            [
                escape('<tr></tr>'),
                'Задает обычную строку'
            ]
        ),
        ContentTableLine(
            [
                escape('<td></td>'),
                'Задает обычную ячейку в строке'
            ]
        ),
        ContentTableLine(
            [
                escape('<th></th>'),
                'Задает заголовочную строку. Может быть помещен внутри <tr></tr>. Для более конкретного назначения заголовка (по типу для кого заголовок: для столбца, строки или еще какой хуйни) рекомендуется использовать атрибут <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th">scope</a>'
            ]
        ),
        ContentTableLine(
            [
                escape('<col></col>'),
                'Позволяет задать параметры для колонок таблицы'
            ]
        ),
        ContentTableLine(
            [
                escape('<caption></caption>'),
                'Позволяет задать заголовок таблицы (будет отображаться снизу)'
            ]
        ),
        ContentTableLine(
            [
                escape('<thead></thead>'),
                escape('Позволяет хранить одну или несколько строк (<tr></tr>), выделяя их, как начальные строки таблицы')
            ]
        ),
        ContentTableLine(
            [
                escape('<tbody></tbody>'),
                escape('Позволяет хранить одну или несколько строк (<tr></tr>), выделяя их, как основную инфу в таблице')
            ]
        ),
        ContentTableLine(
            [
                escape('<tfoot></tfoot>'),
                escape('Позволяет хранить одну или несколько строк (<tr></tr>), выделяя их, как футер таблицы')
            ]
        )
    ]
)

other_tags = ContentTable(
    False,
    ['Тег', 'Атрибуты (если есть)', 'Для чего используется'],
    [
        ContentTableLine(
            [
                escape('<a></a>'),
                'href',
                'Задает ссылку на источник, указанный в href'
            ]
        ),
        ContentTableLine(
            [
                escape('<link></link>'),
                'href, rel',
                'Задает зависимости в документе. href отвечает за источник зависимости, rel — за тип (типа куда ссылка: на css документ, на картинку или еще какую ебень)'
            ]
        ),
        ContentTableLine(
            [
                str(UnorderedList([ escape(elem) for elem in ['<head></head>', '<body></body>', '<footer></footer>']])),
                '',
                'Используются для смысловой разметки документа. head обычно содержит в себе метаинформацию, туда подключаются скрипты и стили. body содержит в себе тело страницы, а footer — информацию о авторе и его контактах'
            ]
        ),
        ContentTableLine(
            [
                escape('<h1></h1>'),
                '',
                'Задают заголовки. Можно использовать h1-h6, тег h6 будет задавать заголовок нижнего уровня'
            ]
        ),
        ContentTableLine(
            [
                escape('<ul></ul>'),
                '',
                'Создает неупорядоченный список'
            ]
        ),
        ContentTableLine(
            [
                escape('<ol></ol>'),
                '',
                'Создает упорядоченный список'
            ]
        ),
        ContentTableLine(
            [
                escape('<li></li>'),
                '',
                'Создает элемент упорядоченного/неупорядоченного списка'
            ]
        ),
        ContentTableLine(
            [
                escape('<pre></pre>'),
                '',
                'Сохраняет формат текста, как он был написан в документе html (например, незначащие пробелы)'
            ]
        ),
        ContentTableLine(
            [
                escape('<text></text>'),
                '',
                'С помощью этого тега принято обрабатывать различные куски текста'
            ]
        ),
        ContentTableLine(
            [
                escape('<p></p>'),
                '',
                'С помощью этого тега принято обрабатывать абзацы текста в документе'
            ]
        )
    ]
)
html_template = escape("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="здесь подключаешь стили">
    <title>Здесь заголовок страницы</title>
</head>
<body>Здесь основной контент страницы</body>
<footer>Здесь всякая инфа по типу контактов</footer>
</html>""")

kwargs = {
    'div_example': escape('<div>some content here</div>'),
    'div_table': div_table,
    'table_attr': table_attr,
    'table_tags': table_tags,
    'other_tags': other_tags,
    'html_template': html_template
}

chapter_list = define_from_html(jinja_templs + '/html_reminder.html')

instruction = Instruction(
    'Html reminder',
    'html_reminder.html',
    kwargs,
    chapter_list
)
instruction.make_static(Path(static_pages, 'html_reminder.html'))
