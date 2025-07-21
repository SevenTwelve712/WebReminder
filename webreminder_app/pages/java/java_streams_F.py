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

FISConstr = """FileInputStream(String fileName) throws FileNotFoundException
FileInputStream(File file) throws FileNotFoundException"""

baseStreamsMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine('InputStream', 'subhead'),
        ContentTableLine(['int available()', 'Возвращает количество байтов, доступных для чтения в потоке']),
        ContentTableLine(['void close()', 'Закрывает поток']),
        ContentTableLine(['int read()', 'Возвращает целочисленное представление следующего байта в потоке или -1 при EOF']),
        ContentTableLine(['void skip(long num)', 'Пропускает number байтов при чтении']),

        ContentTableLine('OutputStream', 'subhead'),
        ContentTableLine(['void close()', 'Закрывает поток']),
        ContentTableLine(['void flush()', 'Очищает буфер ввода, записывая все содержимое в файл']),
        ContentTableLine(['void write(int b)', 'Записывает в поток байт b (представлен как целочисленное)']),

        ContentTableLine('Reader', 'subhead'),
        ContentTableLine(['int read()', 'Возвращает целочисленное представление следующего символа в потоке или -1 при EOF']),
        ContentTableLine(['abstract void close()', 'Закрывает поток']),

        ContentTableLine('Writer', 'subhead'),
        ContentTableLine(['void close()', 'Закрывает поток']),
        ContentTableLine(['void flush()', 'Очищает буфер ввода, записывая все содержимое в файл']),
        ContentTableLine(['void write(int c)', 'Записывает в поток символ c ,представленный целочисленным значением']),
        ContentTableLine(['void write(String s)', 'Записывает в поток строку s'])
    ]
)

FOSConstructor = """FileOutputStream(String fileName) throws FileNotFoundException
FileOutputStream(File file) throws FileNotFoundException"""

FRConstructor = """FileReader(String fileName) 
FileReader(File file)"""

FWConstructor = """FileWriter(String fileName)
FileWriter(File file)"""

OSTable = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(['void close()', 'Закрывает поток']),
        ContentTableLine(['void flush()', 'Сбрасывает буфер, записывает его содержимое в поток']),
        ContentTableLine(['void writeObject(Object obj)', 'Записывает в поток объект'])
    ]
)

ISTable = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(['void close()', 'Закрывает поток']),
        ContentTableLine(['Object readObject()', 'Считывает из потока объект'])
    ]
)

chapter_list = define_from_html("java_streams.html")
kwargs = {
    'Scanner': Scanner,
    'BufferedReader': BufferedReader,
    'BufferedStreamsMethods': BufferedStreamsMethods,
    'PrintWriter': PrintWriter,
    'PrintWriterMethods': PrintWriterMethods,
    'FISConstr': FISConstr,
    'baseStreamsMethods': baseStreamsMethods,
    'FOSConstructor': FOSConstructor,
    'FRConstructor': FRConstructor,
    'FWConstructor': FWConstructor,
    'OSTable': OSTable,
    'ISTable': ISTable
}
instruction = Instruction(
    'Потоки ввода/вывода',
    'java_streams.html',
    kwargs,
    chapter_list
)