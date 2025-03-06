class UnorderedList:
    def __init__(self, content: list[str]):
        """
        Класс неупорядоченного списка (<ul></ul>). Создан для упрощения работы с такими списками
        :param content:
        """
        self.content = content

    def __str__(self):
        return f"<ul>{''.join(['<li>' + elem + '</li>' for elem in self.content])}</ul>"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    test = str(UnorderedList(['function', 'iterable', 'start']))
    print(test)