from markupsafe import escape
from help.support.abspaths import static_pages, jinja_templs
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from pathlib import Path

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

ready_html = escape("""<!--nav_ready.html -->
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
</html>""")

filters_ex = """{{ name|striptags|title }} # Jinja синтаксис
title(striptags(name)) # Python синтаксис
# Результат будет одинаковым"""

tests = """{% if loop.index is divisibleby 3 %}
{% if loop.index is divisibleby(3) %}
# Делают одно и то же"""

whitespaces1 = """{% for item in seq -%}
    {{ item }}
{%- endfor %}"""

escaping = escape("""{% raw %}
    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endraw %}""")

parent_templ = escape("""{# 'parent.html' #}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  {% block head %}
  <link rel="stylesheet" href="parent.css">
  <title>Parent</title>
  {% endblock %}
</head>
<body>
{% block body%}
<p>Hello, child!</p>
{% endblock %}
</body>
</html>""")

child_templ = escape("""{# child.html #}
{% extends 'parent.html' %}
{% block head %}
<link rel="stylesheet" href="child.css">
<title>Child</title>
{% endblock %}
{% block body %}
{{ super() }}
<p>Hi, parent!</p>
{% endblock %}""")

child_ready = escape("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="child.css">
<title>Child</title>
</head>
<body>
<p>Hello, child!</p>
<p>Hi, parent!</p>
</body>
</html>""")

for_ = escape("""{% for item in list %}
<p>{{ item }}, i`m item!</p>
{% endfor %}""")

for_else = escape("""<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% else %}
    <li><em>no users found</em></li>
{% endfor %}
</ul>""")

recursive = escape("""<div class="chapter_list">
    Содержание
		<ol>
            {% for header in chapter_list recursive %}
            <li>
                <a href="#{{ header.id}}">{{ header.text }}</a>
                {% if header.subheads %}
                <ul>
                    {{ loop(header.subheads) }}
                </ul>
                {% endif %}
            </li>
            {% endfor %}
		</ol>
</div>""")

if_ = escape("""{% if blyat %}
<p>blyat</p>
{% elif pizdec %}
<p>pizdec</p>
{% else %}
<p>Seems that everything is ok</p>
{% endif %}""")

macro = escape("""{% macro moan(times) %}
<p>{{ 'ah' * times }}</p>
{% endmacro %}""")

macro_use = """{% from 'moan.html' import moan %}
{{ moan(3) }}"""

macro_res = escape("""<p>ahahah</p>""")

block_assign = escape("""{% set navigation %}
    <li><a href="/">Index</a>
    <li><a href="/downloads">Downloads</a>
{% endset %""")

kwargs = {
    'whitespaces1': whitespaces1,
    'html_jinja_example': html_jinja_example,
    'python_jinja':python_jinja,
    'ready_html': ready_html,
    'filter_ex': filters_ex,
    'tests': tests,
    'escaping': escaping,
    'parent_templ': parent_templ,
    'child_templ': child_templ,
    'child_ready': child_ready,
    'for': for_,
    'if': if_,
    'for_else': for_else,
    'recursive': recursive,
    'macro': macro,
    'macro_use': macro_use,
    'macro_res': macro_res,
    'block_assign': block_assign
}

page = Instruction(
    'jinja2',
    'jinja.html',
    kwargs,
    define_from_html('jinja.html')
)
