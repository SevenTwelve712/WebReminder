from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

base_example = """public class Program{ 
    public static void main (String args[]){
        System.out.println("Hello world!");
    }
}"""
kwargs = {'base_example': base_example}
html_path = 'java/main.html'
chapter_list = define_from_html(html_path)
instruction = Instruction(
    'Основы',
    html_path,
    kwargs,
    chapter_list
)
