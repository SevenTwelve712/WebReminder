from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

if_ = """if (cond) {
    then do;
}
else if (other cond) {
    do smth else;
}
else {
 do else;
 }"""

switch = """switch (var) {
    case 1:
        do smth;
        break;
    case 2:
        do smth else;
        break;
    default:
        do else;
        break;
}"""

simple_switch = """switch (var) {
    case 1 -> do smth;
    case 2 -> do smth else;
    default -> do default;
}"""

ternary = """var var = cond ? then : else;"""

for_ = """// Выведет 712 раз 712
for (int i = 0; i < 712; i++) {
    System.out.println("712");
}"""

while_ = """while (cond) {
    do smth;
}"""

do_while = """do {
    do smth;
}
while (cond);"""

for_iter = """for (var elem : alam_arr) { do smth; }"""

chapter_list = define_from_html("java_cond_expr_loops.html")
kwargs = {
    'if_': if_,
    'switch': switch,
    'simple_switch': simple_switch,
    'ternary': ternary,
    'for_': for_,
    'while_': while_,
    'do_while': do_while,
    'for_iter': for_iter
}
instruction = Instruction(
    'Условные выражения и циклы',
    'java_cond_expr_loops.html',
    kwargs,
    chapter_list
)