from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

comment = """/**
* im a comment
* second line
*/"""

html_path = 'java/documentation.html'
chapter_list = define_from_html(html_path)
kwargs = {
    'comment': comment
}
instruction = Instruction(
    'Документация',
    html_path,
    kwargs,
    chapter_list
)