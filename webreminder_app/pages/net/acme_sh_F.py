from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html


page = Instruction('acme.sh', 'acme_sh.html', {}, define_from_html('acme_sh.html'))
