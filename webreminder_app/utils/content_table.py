from typing import Union


class ContentTableLine:
    def __init__(self, content: Union[list[str], str], type_='usual'):
        """
        Класс одной линии таблицы класса Content Table
        :param content: Что будет записано в строке. Список если это обычная строка, и ничего совмещать не надо.
         Строка, если это подзаголовок
        :param type_: Тип строки: обычный или подзаголовок
        :param show_tags: Будет ли экранировано содержимое линии (если False, то да, иначе нет)
        """
        self.content = content

        if type_ not in ['usual', 'subhead']:
            raise ValueError(f'excepted "usual" or "subhead", got {type_} instead')

        self.type_ = type_

    def __str__(self):
        return f"ContentTableLine(content: {str(self.content)}, type: {self.type_})"

    def __iter__(self):
        return iter(self.content)

    def __repr__(self):
        return f"ContentTableLine(content: {str(self.content)}, type: {self.type_})"


class ContentTable:
    def __init__(self, caption: Union[str, bool], header: list, lines: list[ContentTableLine]):
        """
        Класс таблицы
        :param caption: Подпись таблицы (отображается над самой таблицей)
        :param header: Заголовочная трока таблицы
        :param lines: Список строк таблицы
        """
        self.columns = len(header)
        self.header = header
        self.lines = lines
        self.caption = caption
        self.styles = []

    def __str__(self):
        return f"ContentTable(caption: {self.caption}, header: {self.header}, lines: {str(self.lines)})"

    def __bool__(self):
        return bool(self.lines)

    def get_last(self):
        """
        Возвращает последнюю строку таблицы (необходим, чтобы правильно оформить округление)
        """
        return self.lines[-1]

    def add_styles(self, styles: list[str]):
        """
        В качестве строк списка нужно передавать строку вида "свойство: значение"
        """
        self.styles += styles
