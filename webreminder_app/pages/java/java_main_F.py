from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

base_example = """public class Program{ 
    public static void main (String args[]){
        System.out.println("Hello world!");
    }
}"""
kwargs ={'base_example': base_example}
chapter_list = define_from_html("java_main.html")
instruction = Instruction(
    'Основы',
    'java_main.html',
    kwargs,
    chapter_list
)
