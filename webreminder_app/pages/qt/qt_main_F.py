# -*- coding: utf-8 -*-

from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from webreminder_app.utils.unordered_list import UnorderedList

QWidget = ContentTable(
    False,
    ['Метод', 'Аргументы', 'Что делает'],
    [
        ContentTableLine(
            [
                'QWidget.geometry()',
                str(UnorderedList(['x, y, width, height', 'QRect'])) + 'оба варианта подходят',
                'Возвращает геометрию виджета: левую верхнюю точку (в родительских координатах) и размер'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.layout()',
                '',
                'Возвращает объект-менеджер (layout), который управляет расположением виджетов внутри объекта.'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.move()',
                UnorderedList(['x, y', 'QPoint']),
                'Перемещает виджет в новую позицию: помещает левую верхнюю точку в (x; y) в родительских координатах'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.parentWidget()',
                '',
                'Возвращает родительский виджет, в котором находится текущий виджет. Если виджет не имеет родителя, '
                'возвращает None.'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.repaint()',
                '',
                'Тут же перерисовывает виджет'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.resize()',
                UnorderedList(['width, height', 'QSize']),
                'Изменяет размер виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setGeometry()',
                str(UnorderedList(['x, y, width, height', 'QRect'])) + 'оба варианта подходят',
                'Устанавливает геометрию виджета: помещает его левую верхнюю точку в (x; y) '
                '(в родительских координатах) и задает размер'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setGraphicseffect()',
                'QGraphicsEffect',
                'Устанавливает графический эффект для виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setFixedSize()',
                UnorderedList(['width, height', 'QSize']),
                'Устанавливает фиксированный размер виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setLayout()',
                'layout',
                'Устанавливает объект-менеджер (layout), который управляет расположением виджетов внутри объекта.'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setMaximumSize()',
                UnorderedList(['width, height', 'QSize']),
                'Устанавливает максимальный размер виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setMinimumSize()',
                UnorderedList(['width, height', 'QSize']),
                'Устанавливает минимальный размер виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.size()',
                '',
                'Возвращает текущий размер виджета'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.sizeHint()',
                '',
                'Возвращает предполагаемый размер виджета. Важно прописывать в собственных'
                'виджетах, чтобы приложение понимало, какие размеры занимает виджет'
            ]
        ),
        ContentTableLine(
            [
                'QWidget.setStyleSheet()',
                'str',
                'Устанавливает qss строку в стили виджета'
            ]
        )
    ]
)

main_init = """class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # когда наследуем виджеты от встроенных в Qt лучше всегда это
        # прописывать вначале, для корректной инциализации

        self.clicks = 0

        self.setWindowTitle('Clicker')  # Заголовок, отображается сверху

        self.central_widget = QWidget(self) # Помимо центрального виджета еще может быть menu bar 
        #  и footer, central widget это как body в html документе
        central_layout = QVBoxLayout()
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)  # Сделаем вертикальный layout для виджета,  
        # установим его, а затем скажем главному окну, что у него есть центральный виджет.
        # Весь контент мы теперь будем добавлять не в главное окно, а в центральный виджет
        
        # Я обычно выношу верстку виджетов в отдельные функции, для читабельности
        self.do_click_button()
        self.do_click_counter()"""

start_app = """if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()  # Запускаем цикл событий"""

click_button = """    def do_click_button(self):
        # Сделаем кнопку, по которой будем кликать, не забываем указать родителя
        self.click_button = QPushButton('Click me!', self.central_widget)
        self.click_button.clicked.connect(self.increase_clicks)  # Про сигналы и слоты,
        # отдельная тема. Смотри в след. главах. 
        # Конкретно этот код при нажатии на кнопку коннектится к функции self.increase_clicks
        # Естественно, добавляем кнопку в layout
        self.central_widget.layout().addWidget(self.click_button)"""

click_counter = """    def do_click_counter(self):
        self.click_counter = QLabel('0', self.central_widget)
        self.central_widget.layout().addWidget(self.click_counter)
        self.click_counter.setAlignment(Qt.AlignCenter)"""

back = """    def reset_clicks(self):
        self.clicks = 0
        self.click_counter.setText(str(self.clicks))

    def increase_clicks(self):
        self.clicks += 1
        self.click_counter.setText(str(self.clicks))"""

reset_count = """        self.reset_button = QPushButton('Сбросить клики', self.central_widget)
        self.central_widget.layout().addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.reset_clicks)"""

QLabel = ContentTable(
    False,
    ['Метод', 'Аргументы', 'Что делает'],
    [
        ContentTableLine(
            [
                '__init()__',
                'text, parent',
                'Создает QLabel с заданным текстом и родительским виджетом'
            ]
        ),
        ContentTableLine(
            [
                'alignment()',
                '',
                'Возвращает позиционирование аргумента'
            ]
        ),
        ContentTableLine(
            [
                'setAlignment()',
                'Qt.AlignmentFlag',
                'Устанавливает позиционирование аргумента (например, по центру, или справа, итп)'
            ]),
        ContentTableLine(
            [
                'setScaledContents()',
                'bool',
                'Устанавливает масштабирование содержимого виджета. '
                'При True пытается подогнать картинку под размеры виджета'
            ]
        ),
        ContentTableLine(
            [
                'text()',
                '',
                'Получает текст элемента'
            ]
        ),
        ContentTableLine(
            [
                'setPixmap()',
                'QPixmap',
                'Устанавливает картинку в виджет'
            ]
        ),
        ContentTableLine(
            [
                'pixmap()',
                '',
                'Возвращает картинку в виджете'
            ]
        ),
        ContentTableLine(
            [
                'clear()',
                '',
                'Очищает любой контент виджета'
            ]
        ),
        ContentTableLine(
            [
                'setText()',
                'str',
                'Устанавливает текст аргумента'
            ]
        )
    ]
)

chapter_list = define_from_html("qt_main.html")
kwargs = {
    'QWidget': QWidget,
    "main_init": main_init,
    "start_app": start_app,
    "click_button": click_button,
    "click_counter": click_counter,
    "back": back,
    "reset_count": reset_count,
    "QLabel": QLabel
}

instruction = Instruction(
    'Qt_main',
    'qt_main.html',
    kwargs,
    chapter_list
)