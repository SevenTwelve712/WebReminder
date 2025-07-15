from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

Scanner = """public static void main(String[] args) {
    try(Scanner reader = new Scanner(new FileReader("filename.txt"))) {
        System.out.println(reader.nextLine());
    }

    catch (FileNotFoundException ex) {
        System.out.println(ex.getMessage());
    }
}"""

BufferedReader = """try (BufferedReader reader = new 
        BufferedReader(new FileReader("filename.txt"), 4096)){
    System.out.println(reader.readLine());
}
catch (IOException e) {
    System.out.println(e.getMessage());
}"""

BufferedStreamsMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine('BufferedWriter', type_='subhead'),
        ContentTableLine(['void write(String s)', 'Записывает в поток строку s']),
        ContentTableLine(['void write(int c)', 'Записывает один символ']),
        ContentTableLine(['void newLine()', 'Записывает символ новой строки']),
        ContentTableLine(['flush()', 'Принудительно записывает буфер в поток']),
        ContentTableLine(['close()', 'Закрывает поток']),

        ContentTableLine('BufferedReader', type_='subhead'),
        ContentTableLine(['String readLine()', 'Считывает одну строку текста (удаляет символ переноса строки)']),
        ContentTableLine(['int read()', 'Считывает один символ']),
        ContentTableLine(['void close()', 'Закрывает поток']),
    ]
)

PrintWriterMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(['void println(Smth s)', 'Записывает в поток s с переносом на новую строку']),
        ContentTableLine(['void print(Smth s)', 'Записывает в поток s без символа переноса']),
        ContentTableLine(['void flush()', 'Принудительно записывает буфер в поток']),
        ContentTableLine(['void close()', 'Закрывает поток']),
    ]
)

PrintWriter = """try (PrintWriter writer = new PrintWriter(new
        FileWriter("filename.txt", true))){
    writer.println("some text");
}
catch (IOException e){
    System.out.println(e.getMessage());
}"""

chapter_list = define_from_html("java_streams.html")
kwargs = {
    'Scanner': Scanner,
    'BufferedReader': BufferedReader,
    'BufferedStreamsMethods': BufferedStreamsMethods,
    'PrintWriter': PrintWriter,
    'PrintWriterMethods': PrintWriterMethods
}
instruction = Instruction(
    'Потоки ввода/вывода',
    'java_streams.html',
    kwargs,
    chapter_list
)