from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

comment = """/**
* im a comment
* second line
*/"""

chapter_list = define_from_html("java_documentation.html")
kwargs = {
    'comment': comment
}
instruction = Instruction(
    'Документация',
    'java_documentation.html',
    kwargs,
    chapter_list
)