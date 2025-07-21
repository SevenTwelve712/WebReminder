from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = 'net/acme_sh.html'
page = Instruction('acme.sh', html_path, {}, define_from_html(html_path))
