# Как пользоваться webreminder app
## Quickstart
Запускаем app.py из пакета webreminder_app. Сайт должен запуститься по адресу http://192.168.1.70:7127.
## Как писать
### Про navbar
Объект navbar определен в init wevreminder_app. Для его отображения в статье достаточно в функции render_template() 
указать атрибут navbar:
```python
from webreminder_app import navbar
from flask import render_template

render_template('path/to/template', **some_kwargs, navbar=navbar)
```
Если нужно добавить элемент в navbar, то следует изменять экземпляр класса NavigationBar, лежащий в 
webreminder_app.pages.navigation_bar. Подробнее про NavigationBar смотри в секции utils
### Про библиотеки
Простой пример библиотеки:
* Пишем саму страницу библиотеки
```python
# library_name.py
from webreminder_app.utils.content_table import *
from webreminder_app.utils.libraries_render import LibraryPage

# Экстра инфо для библиотеки (будет отображаться сверху):
extra = ContentTable(False, ['list of headers'], [ContentTableLine(['line_of_content'])])
# Основной контент библиотеки:
content = ContentTable('library_name', ['list of headers'], [ContentTableLine(['line_of_content'])])
# Объект страницы библиотеки
page = LibraryPage('library_name', extra, content)
```
* Добавляем страницу библиотеки в web приложение
```python
# app.py
from flask import Flask, render_template
from webreminder_app.pages.libraries.library_name import page
from webreminder_app import navbar

app = Flask('app_name')


@app.route('/libraries/library_name')
def library_name():
    return render_template('utils/library.html', library=page, navbar=navbar)
# NB: 'utils/library.html' отсылает к шаблону jinja, этот параметр менять не надо
```
Некоторые детали:
+ Для более подробной информации про ContentTable, ContentTableLina, LibraryPage смотри секцию utils
+ Если нужно написать нумерованный список, следует использовать класс UnorderedList из webreminder_app.utils.unordered_list.
Нужно взять str(UnorderedList(['elems']))
### Про инструкции
Простой пример инструкции:
* Пишем тело инструкции (то, что будет внутри страницы)
```html
<!--instruction.html -->
<p>Это ключевое значение 1: {{ kwarg1 }}</p>
<p>Это ключевое значение 2: {{ kwarg2 }}</p>
<p>Вот и все. Хуй тебе, а не инструкция</p>
```
* Пишем страницу инструкции
```python
# instruction.py
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

kwarg1 = "kwarg"
kwarg2 = "krwarg"

chapter_list = define_from_html("instruction.html")
kwargs = {
    'kwarg1': kwarg1,
    'kwarg2': kwarg2
}
instruction = Instruction(
    'name',
    'instruction.html',
    kwargs,
    chapter_list
)
```
* Добавляем инструкцию в веб-приложение
```python
# app.py
from flask import Flask, render_template
import webreminder_app.pages.instructions.instruction
from webreminder_app import navbar

app = Flask('app_name')


@ app.route('instructions/instruction')
def instruction():
    return render_template('utils/instruction.html', instruction=instruction.instruction, navbar=navbar, **instruction.kwargs)
# NB: 'utils/instruction.html' отсылает к шаблону jinja, эту строку менять не надо
```
* Подробнее про используемые классы смотри в разделе utils
* О том, как писать шаблоны jinja смотри в соответствующей странице, она лежит на сайте в /instructions/jinja.html
## Utils
### NAV utils
#### NavElem
NavElem — элементарный объект навигационного окна.
* Аргументы:
  * `name: str` — Имя элемента, т.е. текст, который будет отображаться в окне на сайте
  * `link: Union[str, bool] = True` — ссылка, куда будет вести элемент. 
    * Если указана строка, то ссылка будет вести по 
    `get_url(link)` (get_url — функция создания url по имени функции в Flask)
    * Если True, то создастся ссылка на name `get_url(name)`
    * Если False, то ссылка создаваться не будет
* Методы:
  * `has_link()`: возвращает self.has_link_
#### NavHeaderBlock
NavHeaderBlock — блок навигационного окна, (выпадающий список, грубо говоря) из этих блоков следует составлять само окно
* Аргументы:
  * `header: NavElem` — заголовок навигационного окна (например, *libraries*)
  * `pages: Union[list[NavElem], bool]` — страницы выпадающего списка. Если у блока нет страниц, надо указать False
* Методы:
  * `get_header()`
  * `get_pages()`
  * `add_page(page: NavElem)`: добавляет страницу в self.pages
  * `has_pages()`: возвращает буль, есть ли страницы у блока
#### NavigationBar
NavigationBar — класс навигационного окна
* Аргументы:
  * `headers: list[NavHeaderBlock]` — то, из чего состоит навигационное окно: блоки окна (заголовки)
* Методы:
  * `add_header(header: NavHeaderBlock)`
  * `get_headers()`
  * `render(tabs: int)`: работоспособность этого метода надо проверять, в теории должен выдать html код навигационного окна,
  перед каждой строчкой будет *tab* табуляций

### LIBRARIES utils
