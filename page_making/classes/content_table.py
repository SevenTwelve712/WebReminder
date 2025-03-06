from typing import Union
from jinja2 import FileSystemLoader, Environment, select_autoescape
from help.support.abspaths import jinja_templs


class ContentTableLine:
    def __init__(self, content: Union[list[str], str], type_='usual'):
        """
        Класс одной линии таблицы класса Content Table
        :param content: Что будет записано в строке. Список если это обычная строка, и ничего совмещать не надо.
         Строка, если это подзаголовок
        :param type_: Тип строки: обычный или подзаголовок
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

    def render(self, tabs: int) -> str:
        """
        :return: A html line, where the table is written
        """
        env = Environment(
            loader=FileSystemLoader(jinja_templs),
            autoescape=select_autoescape("html")
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        template = env.get_template('content_table.html')
        rendered = template.render(table=self)
        return '\n'.join(['\t' * tabs + elem for elem in rendered.split('\n')])

    def add_styles(self, styles: list[str]):
        """
        В качестве строк списка нужно передавать строку вида "свойство: значение"
        """
        self.styles += styles


if __name__ == '__main__':
    header = [
        'func', 'what it does'
    ]
    content = [
        ContentTableLine('builtins', 'subhead'),
        ContentTableLine(['print', 'print elem'], 'usual'),
        ContentTableLine(['sorted', 'sorts an iterable'], 'usual'),
        ContentTableLine('end', 'subhead')
    ]
    table = ContentTable(False, header, content)
    table.add_styles(['margin-top: 60px', 'margin-bottom: 60px'])
    print(table.render(tabs=3))
