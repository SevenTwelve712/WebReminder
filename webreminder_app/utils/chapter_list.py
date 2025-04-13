from bs4 import BeautifulSoup
from webreminder_app.configs import LocalDirs


class Header:
    def __init__(self, level: int, text: str, id_: str, subheads: list, parent=None):
        self.level = level
        self.text = text
        self.id = id_
        self.subheads = subheads
        self.parent = parent

    def add_subheader(self, subheader):
        self.subheads.append(subheader)

    def __repr__(self):
        return f"Header(id={self.id}, text={self.text})"

    def set_parent(self, parent):
        self.parent = parent


class ChapterList:
    def __init__(self, headers: list[Header]):
        self.headers = headers

    def add_header(self, header: Header):
        self.headers.append(header)


def define_from_html(path: str):
    """
    Выделяет из html документа заголовки и формирует их структуру
    :param path: Путь к html документу относительно templates/finished
    :return: Список заголовков меньшего уровня. У каждого из них могут быть потомки низшего уровня
    """
    with open(LocalDirs.jinja_templates + '/finished/' + path, encoding='utf_8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    headers = soup.find_all([f"h{i}" for i in range(1, 7)])

    # Заголовки — html теги заголовков, т.е. их уровни могут быть от 1 до 6
    # Пусть parent несуществующий заголовок с невозможно маленьким уровнем.
    # Тогда чисто технически, все оставшиеся заголовки будут его потомками.

    parent = Header(-1, 'parent', 'parent', [])
    current = Header(int(headers[0].name[1]), headers[0].text, headers[0]['id'], [], parent=parent)
    parent.add_subheader(current)

    for header in headers[1:]:
        header = Header(int(header.name[1]), header.text, header['id'], [])
        if header.level > current.level:
            header.set_parent(current)
            current.add_subheader(header)

        elif header.level == current.level:
            header.set_parent(current.parent)
            current.parent.add_subheader(header)

        else:
            curr_parent = current
            while header.level <= curr_parent.level:
                curr_parent = curr_parent.parent  # Пытаемся найти родителя для заголовка

            header.set_parent(curr_parent)
            curr_parent.add_subheader(header)

        current = header

    return parent.subheads


# if __name__ == '__main__':
#     struct = define_from_html('../../test/chapters_test.html')
#     env = Environment(loader=FileSystemLoader('../jinja_templates'))
#     env.trim_blocks = True
#     env.lstrip_blocks = True
#     templ = env.get_template('ct.html')
#     print(templ.render(struct=struct))
