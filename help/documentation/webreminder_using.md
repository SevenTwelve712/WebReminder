# WebReminder App
WebReminder App — проект, созданный как учебник для меня. Объективно, в IT дохуя всего, что надо запомнить, поэтому я создал
этот проект, чтобы документировать мои знания, так или иначе связанные с IT миром.
## Структура проекта
```
help
    -|documentation: различная документация
webreminder_app: основной пакет приложения
    -|pages: готовые скрипты страниц
        -|instructions
        -|libraries
        -|__init__.py
        -|navigation_bar.py: файл навигационного окна
    -|static: различные статичные файлы
        -|fonts: файлы шрифтов
        -|styles: css стили
    -|templates: jinja шаблоны
        -|finished: законченные шаблоны, которые составляют основную часть какой-либо страницы (обычно, инструкций)
        -|utils: шаблоны для шаблонов (макро) и прочая хуйня
    -|utils: пакет утилит, предназначенных для создания страниц
    -|__init__.py: инициализационный файл, в нем инициализируется приложение
    -|configs.py: файл с конфигами, например, абсолютные пути к шаблонам
app.py: файл, в котором запускается приложение (для теста через встроенный flask сервер)
requirements.txt
```
## Как писать
### Про navbar
Объект navbar определен в init webreminder_app. Для его отображения в статье достаточно в функции render_template() 
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
from webreminder_app.utils.table_only import TableOnlyPage

# Экстра инфо для библиотеки (будет отображаться сверху):
extra = ContentTable(False, ['list of headers'], [ContentTableLine(['line_of_content'])])
# Основной контент библиотеки:
content = ContentTable('library_name', ['list of headers'], [ContentTableLine(['line_of_content'])])
# Объект страницы библиотеки
page = TableOnlyPage('library_name', extra, content)
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
    return render_template('utils/table_only.html', library=page, navbar=navbar)
# NB: 'utils/table_only.html' отсылает к шаблону jinja, этот параметр менять не надо
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
* Атрибуты:
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
* Атрибуты:
  * `header: NavElem` — заголовок навигационного окна (например, *libraries*)
  * `pages: Union[list[NavElem], bool]` — страницы выпадающего списка. Если у блока нет страниц, надо указать False
* Методы:
  * `get_header()`
  * `get_pages()`
  * `add_page(page: NavElem)`: добавляет страницу в self.pages
  * `has_pages()`: возвращает буль, есть ли страницы у блока
#### NavigationBar
NavigationBar — класс навигационного окна
* Атрибуты:
  * `headers: list[NavHeaderBlock]` — то, из чего состоит навигационное окно: блоки окна (заголовки)
* Методы:
  * `add_header(header: NavHeaderBlock)`
  * `get_headers()`
  * `render(tabs: int)`: работоспособность этого метода надо проверять, в теории должен выдать html код навигационного окна,
  перед каждой строчкой будет *tab* табуляций
### LIBRARIES utils
####  LibraryPage
LibraryPage — класс страницы библиотеки
* Атрибуты:
  * `library: str`: — имя библиотеки
  * `extra_info: Union[ContentTable, bool]` — дополнительная информация о библиотеке (будет отображаться сверху), если False, 
  то ничего отображаться не будет
  * `content: ContentTable` — сам контент страницы в виде таблицы
### INSTRUCTIONS utils
#### Instruction
Instruction — класс страницы инструкции
* Атрибуты:
  * `name: str` — название инструкции
  * `content: str` — путь до jinja шаблона инструкции (относительно директории jinja_templates)
  * `content_render_kwargs: dict` — необходимые для рендеринга шаблона атрибуты
  * `chapter_kist: dict[str: str]` — словарь заголовков вида {header: header_id}


### CONTENT TABLE utils
#### ContentTableLine
ContentTableLine — класс одной линии таблицы
* Атрибуты:
  * `content: Union[list[str], str]` — сам контент линии.
  * `type_='usual'` — тип линии. Может быть только usual или subhead. Если usual, то при генерации шаблона в строке будут
  несколько ячеек. Причем в i-ой ячейке будет content[i]. Если subhead, то в строке будет одна ячейка с content.
  
    **NB: понятно, что не надо указывать content как строку, если вы хотите сделать ячейку типа usual и наоборот.**
* Методы:
  * ` __str__()`
  * `__iter__()`
  * `__repr__()`
#### ContentTable
ContentTable — класс страницы контента. (красивая таблица с прописанными стилями)
* Атрибуты:
  * `caption: Union[str, bool]` — подпись над таблицей (не то же, что caption в html). Если False, то подписи не будет
  * `header: list` — заголовочная строка таблицы
  * `lines: list[ContentTableLine]` — список строк таблицы
* Методы:
  *  `__str__()`
  * `__bool__()`
  * `get_last()` — возвращает последнюю строку таблицы
  * `add_styles(styles: list[str])` — добавляет стили. В качестве строк списка нужно передавать готовые html стили 
  (т.е. строки должны быть вида `"свойство: значение"`)
