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
        self.styles = ('/code_block.css', '/instructions.css', '/libraries.css', '/navigation.css')
