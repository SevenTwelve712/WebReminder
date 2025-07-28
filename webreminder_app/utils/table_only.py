from typing import Union

from webreminder_app.utils.content_table import ContentTable


class TableOnlyPage:
    def __init__(self, caption: str, extra_info: Union[ContentTable, bool, str], content: ContentTable):
        """
        Класс страницы библиотеки. NB: готовый шаблон страницы (сгенеренный) нужно размещать в директории
        html_elems/static_pages. Иначе документ не найдет стили css
        :param caption: Заголовок таблицы
        :param extra_info: Доп информация по таблице, если False, то игнорируется при рендере
        :param content: Само текло таблицы
        """
        self.name = caption
        self.content = content
        self.extra = extra_info
        self.styles = ('/libraries.css', '/navigation.css')

        if extra_info and not isinstance(extra_info, str):
            # Такой ход конем необходим, тк таблица должна быть отделена от нав окна.
            # Обычно свойством margin-top обладает caption, но тк extra отображается выше его, то приходится прикручивать руками стили
            self.extra.add_styles(['margin-top: 40px'])
