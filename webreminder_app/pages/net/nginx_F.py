from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from webreminder_app.utils.unordered_list import UnorderedList
from webreminder_app.utils.content_table import *

block_dir = """http{
    server{
    }
}"""

main = ContentTable(
    False,
    ['Опция', 'За что отвечает', 'Значение параметров'],
    [
        ContentTableLine(
            [
                'user',
                'От имени какого пользователя будет запускаться Nginx',
                'Строка'
            ]
        ),
        ContentTableLine(
            [
                'worker_processes',
                'Количество запущенных процессов nginx. (устанавливай по количеству ядер проца, если лень парится)',
                'Число'
            ]
        ),
        ContentTableLine(
            [
                'pid',
                'Путь к файлу, где хранится pid главного процесса nginx',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'error_log',
                'Путь к файлу, где будут хранится сообщения об ошибках',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'include',
                'Это особая директива, она может быть использована в любой секции. Включает в конфигурацию другой файл',
                'Путь'
            ]
        ),
    ]
)
events = ContentTable(
    False,
    ['Опция', 'За что отвечает', 'Значение параметров'],
    [
        ContentTableLine(
            [
                'worker_connections',
                'Количество соединений для одного процесса. Как вычислить, читай здесь. '
                'Если не парится, можно выставить значение 1024 если 4 процесса Nginx, 8192 если 1 процесс',
                'Число'
            ]
        )
    ]
)

http_ = ContentTable(
    False,
    ['Опция', 'За что отвечает', 'Значение параметров'],
    [
        ContentTableLine(
            [
                'access_log',
                'Файл, куда будут логироваться запросы',
                'Путь'
            ]
        )
    ]
)

server = ContentTable(
    False,
    ['Опция', 'За что отвечает', 'Значение параметров'],
    [
        ContentTableLine(
            [
                'listen',
                'По какому адресу/порту слушает веб-сервер',
                UnorderedList(['127.0.0.1:80 будет слушать только этот конкретный адрес по 80 порту',
                               '127.0.0.1 будет слушать этот адрес по всем портам',
                               ':80 будет слушать все адреса по 80 порту'])
            ]
        ),
        ContentTableLine(
            ['server_name',
            'Дополнительный инструмент назначения обрабатывающего веб-сервера, если несколько серверов слушают один адрес.'
            'Например, если оба сервера слушают 127.0.0.1:80, один имеет server_name _, а второй server_name www.domen.com. Запрос'
            'www.domen.com/etc будет обрабатываться вторым сервером, а все остальные запросы — первым. (_ никогда не встретится '
            'в доменном имени сервера, поэтому можно его использовать как сервер по умолчанию, он будет обрабатываться последним)',
            'Строка']
        ),
    ]
)

location_ex = """location /{
    root /www;
    index index.html;
}
location /ya_pidor{
    root /pidor_content;
    index pidor_ind.html;
}
location /ya_pidor/gay_porn{
    root /gay_porn;
    index gay_porn.html;
}"""

location = ContentTable(
    False,
    ['Опция', 'За что отвечает', 'Значение параметров'],
    [
        ContentTableLine(
            ['root',
             'Задает директорию, в которой будет искаться uri из запроса. Итого сервером вернется файл root + $uri. В принципе, root '
             'можно использовать в контексте server, но тогда я хз как распределять возвращаемый контент',
             'Путь']
        ),
        ContentTableLine(
            [
                'index',
                'Задает какой файл будет возвращаться, если был задан uri, совпадающий с uri секции location. (вроде бы index это значение по дефолту)',
                'Путь'
            ]
        )
    ]
)

kwargs = {
    "block_dir": block_dir,
    "main": main,
    "events": events,
    "http": http_,
    "server": server,
    "location_ex": location_ex,
    "location": location
}
page = Instruction('nginx', 'nginx.html', kwargs, define_from_html('nginx.html'))
