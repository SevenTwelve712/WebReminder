from webreminder_app.utils.content_table import *
from webreminder_app.utils.table_only import TableOnlyPage
from webreminder_app.utils.unordered_list import UnorderedList

content = ContentTable(
    'os',
    ['Функция или метод', 'Аргументы', 'Смысл', 'Пример использования'],
    [
        ContentTableLine(
            [
                'name',
                'Нет',
                "Возвращает имя операционки. Что может возвращать: 'posix', 'nt' == Windows для пк, 'mac', 'ce' == Windows для калькуляторов и проч. хуеты, 'os2', 'java'",
                "name<hr>'nt'"
            ]
        ),
        ContentTableLine(
            [
                'environ',
                'Нет',
                'Возвращает словарь переменных окружения (можно изменять)',
                "environ<hr>environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\seven\\AppData\\Roaming', ... ебаца длинный словарь ... '_OLD_VIRTUAL_PROMPT': '$P$G'})"
            ]
        ),
        ContentTableLine(
            [
                'getlogin',
                'Нет',
                'Возвращает имя пользователя, вошедшего в систему',
                "getlogin()<hr>'seven'"
            ]
        ),
        ContentTableLine(
            [
                'getpid',
                'Нет',
                'Текущий id процесса',
                'getpid()<hr>9624'
            ]
        ),
        ContentTableLine(
            [
                'access',
                str(UnorderedList(['path', 'mode', 'Всякая херня'])),
                'Чекает уровень доступа у текущего юзера к объекту (директория которого path). Mode = os.F_OK (объект существует) / os.R_OK (доступен на чтение) / os.W_OK (доступен на запись) / os.X_OK (доступен на исполнение). Возвращает true / false',
                'access("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", X_OK)<hr>True'
            ]
        ),
        ContentTableLine(
            [
                'listdir',
                'path',
                'Выдает список из объектов (папок файлов и прочей херни) в path',
                "listdir(path='C:\\Program Files\\Google\\Chrome\\Application)<hr>['115.0.5790.173', 'chrome.exe', 'chrome.VisualElementsManifest.xml', 'chrome_proxy.exe', 'master_preferences', 'SetupMetrics']"
            ]
        ),
        ContentTableLine(
            [
                'mkdir',
                str(UnorderedList(['path', 'Прочая хуета'])),
                'Создает папку по пути path. Если папка есть, то OS error',
                'makedirs("../Frol huesos/1/2")<hr>Теперь на порядок выше есть папка Frol huesos, в которой есть папка 1, в которой есть папка 2'
            ]
        ),
        ContentTableLine(
            [
                'makedirs',
                str(UnorderedList(['path', 'Прочая хуета'])),
                'Создает папку с промежуточными папками. Но никакие из создающихся папок не должны уже быть, иначе OS error',
                'makedirs("../Frol huesos/1/2")<hr>Теперь на порядок выше есть папка Frol huesos, в которой есть папка 1, в которой есть папка 2'
            ]
        ),
        ContentTableLine(
            [
                'remove',
                str(UnorderedList(['path', 'Прочая хуета'])),
                'Удаляет путь к файлу',
                "remove('C:\\test os\\Frol huesos\\1.txt')<hr>Теперь в папке Frol huesos нет файла 1.txt"
            ]
        ),
        ContentTableLine(
            [
                'rename',
                str(UnorderedList(['a', 'b'])),
                'Переименовывает a в b',
                "rename('1.docx', '2.docx')<hr>Теперь файл 1.docx называется 2.docx"
            ]
        ),
        ContentTableLine(
            [
                'system',
                'command',
                'Выполняет системную команду и возвращает код завершения (в случае успеха 0)',
                'system("taskmgr")<hr>Откроет диспетчер задач, а после его закрытия вернет 0'
            ]
        ),
        ContentTableLine(
            [
                'path.abspath',
                'path',
                'Возвращает нормализированный абсолютный путь',
                "ath.abspath('../../Документы')<hr>'C:\\Users\\seven\\Документы'"
            ]
        ),
        ContentTableLine(
            [
                'path.dirname',
                'path',
                'Возвращает путь к родительской директории объекта path',
                'path.dirname("C:\\Users\\seven\\PycharmProjects\\1")<hr>"C:\\Users\\seven\\PycharmProjects"'
            ]
        ),
        ContentTableLine(
            [
                'path.exists',
                'path',
                'Возвращает True если path существует',
                'path.exists("C:\\Users\\seven\\PycharmProjects")<hr>True'
            ]
        ),
        ContentTableLine(
            [
                'path.getatime',
                'path',
                'Время последнего доступа к файлу, в секундах',
                'path.getatime("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>1689501056.968194'
            ]
        ),
        ContentTableLine(
            [
                'path.getmtime',
                'path',
                'Время последнего изменения файла, в секундах',
                'path.getmtime("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>1689013312.5243974'
            ]
        ),
        ContentTableLine(
            [
                'path.getctime',
                'path',
                'Время создания файла (Windows), время последнего изменения файла (Unix)',
                'path.getctime("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>1688768825.913251'
            ]
        ),
        ContentTableLine(
            [
                'path.getsize',
                'path',
                'Размер файла (в байтах)',
                'path.getsize("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>918'
            ]
        ),
        ContentTableLine(
            [
                'path.isabs',
                'path',
                'Проверяет, является ли путь абсолютным',
                'path.isabs("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>True'
            ]
        ),
        ContentTableLine(
            [
                'path.isfile',
                'path',
                'Проверяет, является ли путь файлом',
                'path.isfile("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>True'
            ]
        ),
        ContentTableLine(
            [
                'path.isdir',
                'path',
                'Проверяет, является ли путь директорией',
                'path.isdir("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>False'
            ]
        ),
        ContentTableLine(
            [
                'path.islink',
                'path',
                'Проверяет, является ли путь относительной ссылкой',
                'path.islink("C:\\Users\\seven\\PycharmProjects\\1\\1.py")<hr>False'
            ]
        ),
        ContentTableLine(
            [
                'path.relpath',
                str(UnorderedList(['path', 'start=None'])),
                'Вычисляет путь к path относительно директории start (по умолчанию директория исполняемого файла)',
                'path.relpath("C:\\Users\\seven\\PycharmProjects\\1\\1.py", start="C:\\Program Files")<hr>"..\\Users\\seven\\PycharmProjects\\1\\1.py"'
            ]
        ),
        ContentTableLine(
            [
                'path.samefile',
                str(UnorderedList(['path1', 'path2'])),
                'Проверяет, указывают ли path1 и path2 на один и тот же объект',
                'path.samefile("..\\..\\..\\..\\Иконки\\17.ico", "C:\\Иконки\\17.ico")<hr>True'
            ]
        )
    ]
)

page = TableOnlyPage('os', False, content)