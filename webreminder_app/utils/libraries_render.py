from typing import Union

from webreminder_app.utils.content_table import ContentTable


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
        self.styles = ('/libraries.css', '/navigation.css')

        if extra_info:
            # Такой ход конем необходим, тк таблица должна быть отделена от нав окна.
            # Обычно свойством margin-top обладает caption, но тк extra отображается выше его, то приходится прикручивать руками стили
            self.extra.add_styles(['margin-top: 40px'])
