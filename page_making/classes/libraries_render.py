from page_making.classes.content_table import ContentTable
from page_making.finished_structures.navigation_bar_F import navbar_f
from typing import Union
from pathlib import Path
from help.support.abspaths import html_styles, jinja_templs
from jinja2 import Environment, FileSystemLoader, select_autoescape


class LibraryPage:
    def __init__(self, library: str, extra_info: Union[ContentTable, bool], content: ContentTable):
        """
        Класс страницы библиотеки. NB: готовый шаблон страницы (сгенеренный) нужно размещать в директории
        html_elems/static_pages. Иначе документ не найдет стили css
        :param library: Название библиотеки
        :param extra_info: Доп информация по библиотеке, если False, то игнорируется при рендере
        :param content: Таблица с функциями
        """
        self.name = library
        self.content = content
        self.extra = extra_info
        self.styles = [html_styles + style for style in ('/libraries.css', '\\navigation.css')]

        if extra_info:
            # Такой ход конем необходим, тк таблица должна быть отделена от нав окна.
            # Обычно свойством margin-top обладает caption, но тк extra отображается выше его, то приходится прикручивать руками стили
            self.extra.add_styles(['margin-top: 40px'])

    def render(self):
        env = Environment(
            loader=FileSystemLoader(jinja_templs),
            autoescape=select_autoescape('html')
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        template = env.get_template('library.html')
        return template.render(
            library=self,
            navbar=navbar_f
        )

    def make_static(self, path_to_file: Path):
        """
        Сохраняет сгенерированный документ в html файле
        :param path_to_file: Путь к файлу
        """
        if path_to_file.parts[-2] != 'static_pages':
            raise ValueError('all rendered html pages must be in html_elems/static_pages')

        with open(path_to_file, 'w', encoding='utf-8') as f:
            f.write(self.render())
