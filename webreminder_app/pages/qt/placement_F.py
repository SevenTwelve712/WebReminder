from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

bad_visible = """from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello World!")
        self.setCentralWidget(self.label)
        self.label1 = QLabel('im visible', self.label)
        self.label2 = QLabel('im invisible')
        self.label2.show()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
"""

html_path = 'qt/placement.html'
chapter_list = define_from_html(html_path)
kwargs = {
    "bad_visible": bad_visible
}
instruction = Instruction(
    'Размещение, наследование, отображение',
    html_path,
    kwargs,
    chapter_list
)