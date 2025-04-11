#  Документацию по классам навигационного окна смотри по
#  https://www.figma.com/board/YSDgLQc41v3kPttlXHCh8b/NavBar?t=x0156PuqLPOEFyyH-6
from typing import Union
from jinja2 import Environment, select_autoescape, FileSystemLoader
from webreminder_app.configs import LocalDirs


class NavElem:
    def __init__(self, name: str, link: Union[str, bool] = True):
        """
        Низший элемент навигационного окна
        :param name: То, как элемент будет отображаться в окне
        :param link: Если True, то элемент будет со ссылкой на страницу, причем ссылка будет вычисляться по имени элемента.
        Если False, то ссылки никуда не будет. Если строка, то ссылка будет вычисляться по этому параметру
        """
        self.name = name
        self.has_link_ = bool(link)
        if link is True:
            self.link = name

        elif link is False:
            self.link = None

        else:
            self.link = link

    def has_link(self):
        return self.has_link_

    def __repr__(self):
        return f"NavElem(name: {self.name}, path: {str(self.path)}"


class NavHeaderBlock:
    def __init__(self, header: NavElem, pages: Union[list[NavElem], bool]):
        """
        Один из заголовков навигационного окна
        :param header: Название элемента
        :param pages: Страницы в элементе. Если False, то считается, что заголовок не имеет страниц
        """

        self.header = header
        self.pages = pages

    def __repr__(self):
        return f"Class NavBarHeader(header: {self.header}, pages: {str(self.pages)})"

    def get_header(self):
        return self.header

    def get_pages(self):
        return self.pages

    def add_page(self, page: NavElem):
        self.pages.append(page)

    def has_pages(self):
        return bool(self.pages)


class NavigationBar:
    def __init__(self, headers: list[NavHeaderBlock]):
        """
        Класс навигационного окна
        """
        self.headers = headers

    def __repr__(self):
        return f"Class NavigationBar(headers={str(self.headers)})"

    def add_header(self, header: NavHeaderBlock):
        if header in self.headers:
            raise KeyError(f'Header {header} already in table')

        self.headers.append(header)

    def get_headers(self):
        return self.headers

    def render(self, tabs: int) -> str:
        env = Environment(
            autoescape=select_autoescape('html'),
            loader=FileSystemLoader(LocalDirs.jinja_templates + '/utils')
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        templ = env.get_template('nav_bar.html')
        rendered = templ.render(navbar=self)
        return '\n'.join(['\t' * tabs + elem for elem in rendered.split('\n')])


# tests
if __name__ == '__main__':
    content = [
        NavHeaderBlock(
            NavElem('Главная', False),
            False
        ),
        NavHeaderBlock(
            NavElem('Библиотеки', 'lybraries.html'),
            [
                NavElem('Csv', 'csv.html'),
                NavElem('Functools', 'functools.html'),
                NavElem('Itertools', 'itertools.html')
            ]
        ),
        NavHeaderBlock(
            NavElem('Инструкции', 'list_of_instructions.html'),
            [
                NavElem('Telebot', 'telebot.html')
            ]
        )
    ]
    bar = NavigationBar(content)