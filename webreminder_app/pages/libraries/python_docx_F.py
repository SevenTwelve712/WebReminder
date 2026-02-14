from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

path = "libraries/python_docx.html"
chapter_list = define_from_html(path)

set_attr = '''element = p._element
element.set(qn("w:val"), "42")'''

append_elem = '''tPr = table._tbl.tblPr # xml объект
tblW = OxmlElement("w:tblW")
tblW.set(qn("w:type"), "auto" if auto else "dxa")
tblW.set(qn("w:w"), width)
tPr.append(tblW)'''

find_first = '''tPr = table._tbl.tblPr
tblW = tPr.find(qn("w:tblW"))'''

kwargs = {
    "set_attr": set_attr,
    "append_elem": append_elem,
    "find_first": find_first
}

instruction = Instruction(
    "python-docx",
    path,
    kwargs,
    chapter_list
)