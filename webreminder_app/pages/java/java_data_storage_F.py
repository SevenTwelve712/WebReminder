from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from markupsafe import escape

arrays = escape("""public class Arrays {
    public static void main(String[] args) {
        int[] array = new int[5]; // новый массив длиной 5
        for (int i = 0; i < 5; i++){
            array[i] = i; // обращение к элементам
        }
        int[] array_ = {6, 7, 8, 9, 10}; // создание + инициализация
        System.out.println(java.util.Arrays.toString(array)); // [0, 1, 2, 3, 4]
        System.out.println(java.util.Arrays.toString(array_)); // [6, 7, 8, 9, 10]
    }
}
""")

arrayList = escape("""ArrayList<Integer> nums = new ArrayList<>(5) // создает список емкостью 5 (может расширяться);
nums.add(5);
nums.add(2);
System.out.println(nums); // [5, 2]""")

arrayListMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(
            [
                'void add(int index, E obj)',
                'Добавляет по индексу index элемент obj'
            ]
        ),
        ContentTableLine(
            [
                escape('boolean addAll(int index, Collection<? extends E> col)'),
                'Добавляет по индексу index (если не указан, то в конец) все элементы из col. Если список изменился, возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'E get(int index)',
                'Возвращает index элемент списка'
            ]
        ),
        ContentTableLine(
            [
                'int indexOf(Object obj)',
                'Возвращает индекс первого вхождения объекта в список (-1 если не найден)'
            ]
        ),
        ContentTableLine(
            [
                'int lastIndexOf(Object obj)',
                'Возвращает индекс последнего вхождения объекта в список, -1 если не найден'
            ]
        ),
        ContentTableLine(
            [
                'E remove(int index)',
                'Удаляет и возвращает элемент по индексу index'
            ]
        ),
        ContentTableLine(
            [
                'E set(int index, E obj)',
                'Заменяет элемент по индексу index на obj и возвращает старый элемент'
            ]
        ),
        ContentTableLine(
            [
                escape('void sort(Comparator<? super E> comp)'),
                'Сортирует список по компаратору comp. Для сортировки дефолтных типов можно использовать встроенный компаратор: Comparator.naturalOrder() или '
                'Comparator.reverseOrder()'
            ]
        ),
    ]
)

HashSet = escape("""import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;

public class Arrays {
    public static void main(String[] args) {
        Collection<Integer> numsArr = new ArrayList<>();
        for (int i = 1; i <= 5; i++) { numsArr.add(i); }
        HashSet<Integer> numsSet = new HashSet<>(); // пустое множество
        HashSet<Integer> numsSet_ = new HashSet<>(numsArr); // [1, 2, 3, 4, 5]
        /* Создаст множество емкостью 5, которое будет расширяться при заполнении на 70% */
        HashSet<Integer> numsSet__ = 
                new HashSet<Integer>(5, 0.7f);
    }
}
""")

CollectionMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(
            [
                'boolean add(E item)',
                'Добавляет элемент в коллекцию, при удачном добавлении возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                escape('boolean addAll(Collection <? extends E>'),
                'Добавляет в коллекцию все элементы другой коллекции'
            ]
        ),
        ContentTableLine(
            [
                'void clear()',
                'Удаляет все элементы коллекции'
            ]
        ),
        ContentTableLine(
            [
                'boolean contains (Object item)',
                'Возвращает true если элемент в коллекции, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'boolean isEmpty()',
                'Возвращает true если коллекция пуста, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'boolean remove(Object item)',
                'Удаляет элемент из коллекции, если он есть, возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'boolean removeAll(Collection <?>)',
                'Удаляет все элементы коллекции из коллекции, если они есть, возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'boolean retainAll(Collection <?>)',
                'Удаляет все элементы коллекции, кроме тех, которые есть в аргументе, возвращает true если колекция изменилась, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'int size()',
                'Возвращает размер коллекции'
            ]
        ),
        ContentTableLine(
            [
                'Object[] toArray()',
                'Возвращает массив с элементами коллекции'
            ]
        )
    ]
)

MapMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(
            [
                'void clear()',
                'Очищает коллекцию'
            ]
        ),
        ContentTableLine(
            [
                'boolean containsKey(Object k)',
                'Возвращает утверждение, что коллекция содержит ключ k'
            ]
        ),
        ContentTableLine(
            [
                'boolean containsValue(Object v)',
                'Возвращает утверждение, что коллекция содержит значение v'
            ]
        ),
        ContentTableLine(
            [
                'boolean isEmpty()',
                'Возвращает утверждение "коллекция пуста"'
            ]
        ),
        ContentTableLine(
            [
                'V get(Object k)',
                'Возвращает значение, связанное с ключом k или null'
            ]
        ),
        ContentTableLine(
            [
                'V getOrDefault(Object k, V def)',
                'Возвращает значение, связанное с ключом k или значение по умолчанию def'
            ]
        ),
        ContentTableLine(
            [
                'V put(K k, V v)',
                'Добавляет пару ключ-значение в коллекцию, если ключ уже есть, то заменяет значение, возвращает предыдущее значение v по ключу k или null'
            ]
        ),
        ContentTableLine(
            [
                'V putIfAbsent(K k, V v)',
                'Добавляет пару ключ-значение в коллекцию, если ключ уже есть, то ничего не делает, возвращает значение v по ключу k или null'
            ]
        ),
        ContentTableLine(
            [
                'V remove(Object k)',
                'Удаляет пару ключ-значение из коллекции, возвращает значение'
            ]
        ),
        ContentTableLine(
            [
                'int size()',
                'Возвращает размер коллекции'
            ]
        ),
        ContentTableLine(
            [
                escape('Collection<K> keySet()'),
                'Возвращает коллекцию ключей'
            ]
        ),
        ContentTableLine(
            [
                escape('Collection<V> values()'),
                'Возвращает коллекцию значений'
            ]
        )
    ]
)

HashMap = escape("Map<Integer, String> states = new HashMap<Integer, String>();")

ArrayDequeMethods = ContentTable(
    False,
    ['Метод', 'Что делает'],
    [
        ContentTableLine(
            [
                'void addFirst(E e)',
                'Добавляет элемент в начало'
            ]
        ),
        ContentTableLine(
            [
                'void addLast(E e)',
                'Добавляет элемент в конец'
            ]
        ),
        ContentTableLine(
            [
                'boolean offerFirst(E e)',
                'Добавляет элемент в начало, если удалось, возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'boolean offerLast(E e)',
                'Добавляет элемент в конец, если удалось, возвращает true, иначе false'
            ]
        ),
        ContentTableLine(
            [
                'E getFirst()',
                'Возвращает первый элемент, если коллекция пуста, генерирует NoSuchElementException'
            ]
        ),
        ContentTableLine(
            [
                'E getLast()',
                'Возвращает последний элемент, если коллекция пуста, генерирует NoSuchElementException'
            ]
        ),
        ContentTableLine(
            [
                'E peekFirst()',
                'Возвращает первый элемент (или null)'
            ]
        ),
        ContentTableLine(
            [
                'E peekLast()',
                'Возвращает последний элемент (или null)'
            ]
        ),
        ContentTableLine(
            [
                'E pollFirst()',
                'Возвращает и удаляет первый элемент, если коллекция пуста, возвращает null'
            ]
        ),
        ContentTableLine(
            [
                'E pollLast()',
                'Возвращает и удаляет последний элемент, если коллекция пуста, возвращает null'
            ]
        ),
        ContentTableLine(
            [
                'E pop()',
                'Возвращает и удаляет первый элемент, если коллекция пуста, вызывает исключение NoSuchElementException'
            ]
        ),
        ContentTableLine(
            [
                'void push(E e)',
                'Добавляет элемент в начало'
            ]
        ),
        ContentTableLine(
            [
                'E removeFirst()',
                'Возвращает и удаляет первый элемент, если коллекция пуста, генерирует исключение NoSuchElementException'
            ]
        ),
        ContentTableLine(
            [
                'E removeLast()',
                'Возвращает и удаляет последний элемент, если коллекция пуста, генерирует исключение NoSuchElementException'
            ]
        )
    ]
)

chapter_list = define_from_html("java_data_storage.html")
kwargs = {
    'arrays': arrays,
    'arrayList': arrayList,
    'arrayListMethods': arrayListMethods,
    'HashSet': HashSet,
    'CollectionMethods': CollectionMethods,
    'MapMethods': MapMethods,
    'HashMap': HashMap,
    'ArrayDequeMethods': ArrayDequeMethods
}

instruction = Instruction(
    'Методы хранения данных',
    'java_data_storage.html',
    kwargs,
    chapter_list
)