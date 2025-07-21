from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = 'java/oop.html'
chapter_list = define_from_html(html_path)

constructor = """class Animal{
    String name;
    int age;
    /*Конструктор*/
    Animal(String name, int age){
        this.name = name;
        this.age = age;
    }
    /*Конец конструктора*/
}"""

initialization = """class Person{
    String name;    // имя
    int age;        // возраст
    /*начало блока инициализатора*/
    {
        name = "Undefined";
        age = 18;
    }
    /*конец блока инициализатора*/
}"""

class_ = """class Class {}"""

abstract = """abstract class Abstract {}"""

interface = """interface Interface {}"""

enums = """enum Day{
  
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}"""

methods = """[модификатор доступа] [static] тип_возвращаемого значения имя_метода(аргументы) {}"""

enum_constr = """enum Color{
    RED("#FF0000"), BLUE("#0000FF"), GREEN("#00FF00");
    private String code;
    Color(String code){
        this.code = code;
    }
    public String getCode(){ return code;}
}"""

const_methods = """enum Operation{
    SUM{
        public int action(int x, int y){ return x + y;}
    },
    SUBTRACT{
        public int action(int x, int y){ return x - y;}
    },
    MULTIPLY{
        public int action(int x, int y){ return x * y;}
    };
    public abstract int action(int x, int y);
}"""

generic = """public class generic {
    public static void main(String[] args) {
        ID<String> idd = new ID<>("qwerty");
        System.out.println(idd.getId_());
    }
}

class ID<type>{
    type id_;
    ID(type id_){this.id_ = id_;}

    public type getId_() {
        return id_;
    }
}"""

records = """public class Records {
    public static void main(String[] args) {
        Person Gleb = new Person("Gleb", 18);
        Gleb.age(); // Gleb
        Gleb.name(); // 18
    }
}

record Person (String name, int age) {}"""

kwargs = {
    "records": records,
    "generic": generic,
    "const_methods": const_methods,
    "enum_constr": enum_constr,
    "enums": enums,
    "interface": interface,
    "abstract": abstract,
    "class_": class_,
    "initialization": initialization,
    "constructor": constructor,
    "methods": methods
}

instruction = Instruction(
    'ООП',
    html_path,
    kwargs,
    chapter_list
)