from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

PressableButtonWidget = """class PressableButtonWidget(QPushButton):
    def __init__(self, text, parent):
        # не забываем сразу же сделать инициализацию родительского класса
        super().__init__(text, parent)

        # Инициализируем анимацию при инициализации объекта, так
        # как наша анимация переиспользуема, и нет смысла инициализировать
        # ее каждый раз при нажатии кнопки.

        # Рассчитаем новый размер прямоугольника, а затем просто
        # будем анимировать кнопку от старого размера к новому
        self.old_rect = self.rect()
        cx, cy = self.rect().center().x(), self.rect().center().y()  # center_x, center_y
        scale = 0.92
        new_width = self.old_rect.width() * scale
        new_height = self.old_rect.height() * scale

        self.new_rect = QRect(
            int(cx - new_width // 2),
            int(cy - new_height // 2),
            int(new_width),
            int(new_height)
        )

        # Создадим последовательную группу анимаций: нам сначала
        # нужно проиграть анимацию сужения кнопки, затем расширения
        self.anim_group = QSequentialAnimationGroup()

        self.anim_there = QPropertyAnimation(self, b'geometry', self)
        self.anim_there.setStartValue(self.old_rect)
        self.anim_there.setEndValue(self.new_rect)
        self.anim_there.setDuration(75)

        self.anim_back = QPropertyAnimation(self, b'geometry', self)
        self.anim_back.setStartValue(self.new_rect)
        self.anim_back.setEndValue(self.old_rect)
        self.anim_back.setDuration(75)

        self.anim_group.addAnimation(self.anim_there)
        self.anim_group.addAnimation(self.anim_back)

    def mousePressEvent(self, e: QMouseEvent, /) -> None:
        # При нажатии на кнопку мышкой, запустим анимацию,
        # предварительно остановив предыдущую группу, если она
        # еще играется
        self.anim_group.stop()
        self.anim_group.start()

        # И, конечно, не забываем передать событие в родительский класс
        super().mousePressEvent(e)"""

do_click_button = """    def do_click_button(self):
        # Сделаем оболочку кнопки
        click_button_shell = QWidget(self.central_widget)

        # Помним, что мы не можем диктовать размеры компоновщику,
        # мы можем лишь указать максимальные/минимальные. По дефолту QWidget
        # создастся небольшого размера, возможно вообще нулевого. Поэтому в нормальном
        # проекте придется думать, как прописать ему нормальный размер.
        # Здесь же можно ограничиться таким костылем.
        click_button_shell.setMinimumSize(100, 40)

        # Делаем саму кнопку, затем подгоняем ее размеры. Обратите внимание,
        # что родитель кнопки — оболочка, а не центральный виджет
        self.click_button = PressableButtonWidget('Click me!', click_button_shell)
        self.click_button.setGeometry(0, 0, self.click_button.size().width(), 
                                      self.click_button.size().height())
        self.click_button.clicked.connect(self.increase_clicks)
        self.central_widget.layout().addWidget(click_button_shell)  # Добавляем оболочку в layout"""

do_reset_button = """    def do_reset_button(self):
        # То же самое делаем и с нижней кнопкой 
        reset_button_shell = QWidget(self.central_widget)
        reset_button_shell.setMinimumSize(100, 40)
        self.reset_button = PressableButtonWidget('Сбросить клики', reset_button_shell)
        self.reset_button.setGeometry(0, 0, self.reset_button.size().width(), 
                                      self.reset_button.size().height())
        self.central_widget.layout().addWidget(reset_button_shell)
        self.reset_button.clicked.connect(self.reset_clicks)"""

custom_property = """from PySide6.QtCore import Property


class CustomPropertyClass:
    def __init__(self, value: int):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value

    value = Property(int, get_value, set_value)"""

html_path = 'qt/animations.html'
chapter_list = define_from_html(html_path)
kwargs = {
    'PressableButtonWidget': PressableButtonWidget,
    'do_click_button': do_click_button,
    'do_reset_button': do_reset_button,
    'custom_property': custom_property
}

instruction = Instruction(
    'Animations',
    html_path,
    kwargs,
    chapter_list
)