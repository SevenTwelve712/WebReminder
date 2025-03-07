from jinja2 import Environment, select_autoescape, FileSystemLoader
from help.support.abspaths import html_styles, jinja_templs
from page_making.finished_structures.navigation_bar_F import navbar_f
from pathlib import Path


class Instruction:
    def __init__(self, name: str, content: str, content_render_kwargs: dict, chapter_list: dict[str, str]):
        """
        Класс страницы инструкции
        :param name: Название инструкции
        :param content: Путь до jinja-шаблона инструкции относительно директории jinja_templates
        :param content_render_kwargs: Аргументы, необходимые для генерации шаблона контента
        :param chapter_list: {заголовок: его id}
        """
        self.name = name
        self.content = content
        self.content_kwargs = content_render_kwargs
        self.chapter_list = chapter_list
        self.styles = [html_styles + elem for elem in ('/code_block.css', '/instructions.css', '/libraries.css', '/navigation.css')]

    def render(self):
        env = Environment(
            loader=FileSystemLoader(jinja_templs),
            autoescape=False
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        template = env.get_template('instruction.html')
        return template.render(
            instruction=self,
            navbar=navbar_f,
            **self.content_kwargs
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
