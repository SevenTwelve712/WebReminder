from jinja2 import Environment, select_autoescape, FileSystemLoader
from help.support.abspaths import html_styles, jinja_templs
from page_making.finished_structures.navigation_bar_F import navbar_f


class Instruction:
    def __init__(self, name: str, content: str, content_render_kwargs: dict, chapter_list: dict[str, str]):
        """
        Класс страницы инструкции
        :param name: Название инструкции
        :param content: Путь до jinja-шаблона инструкции
        :param content_render_kwargs: Аргументы, необходимые для генерации шаблона контента
        :param chapter_list: {заголовок: его id}
        """
        self.name = name
        self.content = content
        self.content_kwargs = content_render_kwargs
        self.chapter_list = chapter_list
        self.styles = []

    def render(self):
        env = Environment(
            autoescape=select_autoescape('html'),
            loader=FileSystemLoader(jinja_templs)
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        template = env.get_template('instruction.html')
        return template.render(
            instruction=self,
            nav_bar=navbar_f,
            **self.content_kwargs
        )
