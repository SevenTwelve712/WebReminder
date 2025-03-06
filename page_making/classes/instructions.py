from jinja2 import FileSystemLoader, Environment, select_autoescape
from help.support.abspaths import jinja_templs, html_styles
from typing import Union
from page_making.classes.content_table import ContentTable
from pathlib import Path
from page_making.finished_structures.navigation_bar_F import navbar_f


class InstructionContentElem:
    def __init__(self, type_: str, content: Union[str, list[str], ContentTable, None]):
        """
        Класс контента инструкии
        :param type_: тип контента
        :param content: сам контент

        Допустимые type_ и что они означают:
         table: объект класса ContentTable, означает таблицу
         open_p: любое значение, означает начало параграфа
        end_p: любое значение, означает конец параграфа
         p: текст, означает новый параграф
         open_ul: любое значение, означает старт ненумерованного списка
         end_ul: любое значение, означает конец ненумерованного списка
         open_ol: любое значение, означает старт нумерованного списка
         end_ol: любое значение, означает конец нумерованного списка
         li: текст, означает элемент списка
         code: текст, код, который будет оформлен в соответствии нужному стилю
         hn: список вида [заголовок: id], добавляет заголовок
         a: [текст, куда ведет ссылка], добавляет ссылку
         plain_text: text. Вставляет просто текст
        """
        possible_types = ['table', 'open_p', 'end_p' 'open_ul', 'end_ul', 'li', 'code', 'a', 'open_ol', 'end_ol', 'plain_text'] + [f"h{i}" for i in range(1, 7)]
        if type_ not in possible_types:
            raise ValueError(f"type of elem must be from these: {possible_types}, got {type_} instead")

        self.content = content
        self.type = type_


class Instruction:
    def __init__(self, name: str, content: list[InstructionContentElem]):
        """
        Класс страницы инструкции
        :param name: Название инструкции
        :param content: Контент в виде словаря
        """
        self.name = name
        self.content = content
        self.styles = [html_styles + elem for elem in ('/code_block.css', '/instructions.css', '/libraries.css', '/navigation.css')]
        self.chapter_list = {elem.content[0]: elem.content[1] for elem in content if elem.type in [f"h{i}" for i in range(1, 7)]}

    def open_p(self):
        self.content.append(InstructionContentElem('open_p', None))

    def close_p(self):
        self.content.append(InstructionContentElem('close_p', None))

    def open_ul(self):
        self.content.append(InstructionContentElem('open_ul', None))

    def close_ul(self):
        self.content.append(InstructionContentElem('close_ul', None))

    def open_ol(self):
        self.content.append(InstructionContentElem('open_ol', None))

    def close_ol(self):
        self.content.append(InstructionContentElem('close_ol', None))

    def a(self, text: str, link: str):
        self.content.append(InstructionContentElem('a', [text, link]))

    def code(self, code: str):
        self.content.append(InstructionContentElem('code', code))

    def h(self, level: int, text: str, id_: str):
        header = f"h{level}"
        self.content.append(InstructionContentElem(header, [text, id_]))
        self.chapter_list[header] = id_

    def li(self, text: str):
        self.content.append(InstructionContentElem('li', text))

    def table(self, table: ContentTable):
        self.content.append(InstructionContentElem('table', table))

    def plain_text(self, text: str):
        self.content.append(InstructionContentElem('plain_text', text))

    def render(self):
        env = Environment(
            autoescape=select_autoescape('html'),
            loader=FileSystemLoader(jinja_templs)
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        template = env.get_template('instruction.html')
        return template.render(instruction=self, navbar=navbar_f)

    def make_static(self, path_to_file: Path):
        """
        Сохраняет сгенерированный документ в html файле
        :param path_to_file: Путь к файлу
        """
        if path_to_file.parts[-2] != 'static_pages':
            raise ValueError('all rendered html pages must be in html_elems/static_pages')

        with open(path_to_file, 'w', encoding='utf-8') as f:
            f.write(self.render())
