from help.support.escape import escape
from page_making.classes.content_table import *

html_jinja_example = escape("""<!-- navigation.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ content }}

    {# a comment #}
</body>
</html>""")

python_jinja = """# python script
from jinja2 import Environment, FileSystemLoader


class Nav:
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption


navigation = [Nav('csv.html', 'csv'), Nav('json.html', 'json'), Nav('itertools.html', 'itertools')]
env = Environment(loader=FileSystemLoader('.'))
env.trim_blocks = True
env.lstrip_blocks = True
tempate = env.get_template('navigation.html')
with open('nav_ready.html', 'w') as f:
    f.write(tempate.render(navigation=navigation, content='i`m content'))
"""

ready_html = """<!--nav_ready.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
        <li><a href="csv.html">csv</a></li>
        <li><a href="json.html">json</a></li>
        <li><a href="itertools.html">itertools</a></li>
    </ul>

    <h1>My Webpage</h1>
    i`m content

</body>
</html>"""

expressions = ContentTable(
    False,
    ['Синтаксис', 'Аналог в питоне'],
    [
        ContentTableLine(
            [
                '{% if ... %} ... {% endif %}',
                'if ...:'
            ]
        ),
        ContentTableLine(
            [
                '{% for ... in ... %} ... {% endfor %}',
                'for ... in ...:'
            ]
        ),
        ContentTableLine(
            [
                ''
            ]
        )
    ]
)









