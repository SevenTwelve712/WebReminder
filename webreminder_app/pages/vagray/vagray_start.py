from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

chapter_list = define_from_html("vagray/vagray_start.html")
kwargs = {
}
instruction = Instruction(
    'vagray',
    'vagray/vagray_start.html',
    kwargs,
    chapter_list
)
