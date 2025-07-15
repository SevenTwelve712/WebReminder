from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

try_catch = """import java.util.Scanner;

public class TryCatch {
    public static void main(String[] args) {
        int x, y;
        Scanner in = new Scanner(System.in);
        x = in.nextInt();
        y = in.nextInt();

        try { // пробуем делить
            System.out.println(x / y);
        }

        catch (Exception ex){ // ловим деление на ноль
            System.out.println(ex.getMessage());
        }

        finally { // в любом случае выводим x, y
            System.out.println(x);
            System.out.println(y);
        }
    }
}
"""

throw = 'throw new Exception("Текст исключения");'

tryWithResources = """try (FileWriter writer = new FileWriter("someFilename.txt")){ 
    // определяем поток в скобках после try
    some actions;
}
catch (IOException e){ // ловим возможные исключения
    System.out.println(e.getMessage());
}"""

chapter_list = define_from_html("java_exceptions.html")
kwargs = {
    'try_catch': try_catch,
    'throw': throw,
    'tryWithResources': tryWithResources
}
instruction = Instruction(
    'Исключения и ошибки',
    'java_exceptions.html',
    kwargs,
    chapter_list
)