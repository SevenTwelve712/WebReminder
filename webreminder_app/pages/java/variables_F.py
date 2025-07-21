from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

variables = """int x;
x = 10;
// или
int x = 10;
// можно инициализировать несколько переменных одного типа
//(но не назначать значения)
int x, y;"""

constants = """final double P = 3.14;"""
new = "MyClass obj = new MyClass(args);"

html_path = 'java/variables.html'
chapter_list = define_from_html(html_path)
kwargs = {
    'variables': variables,
    'constants': constants,
    "new": new
}
instruction = Instruction(
    'Переменные и работа с ними',
    html_path,
    kwargs,
    chapter_list
)
