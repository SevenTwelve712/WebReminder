from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html
from webreminder_app.utils.unordered_list import UnorderedList
from webreminder_app.utils.content_table import *
from markupsafe import escape

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
                'Задает какой файл будет возвращаться, если пользователь обратился в каталог, а не к файлу',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'allow',
                'Разрешает доступ с определенных ip адресов',
                'адрес/сеть/all'
            ]
        ),
        ContentTableLine(
            [
                'deny',
                'Запрещает доступ с определенных ip адресов',
                'адрес/сеть/all'
            ]
        )
    ]
)

proxy = ContentTable(
    False,
    ['Директива', 'За что отвечает', 'Значение'],
    [
        ContentTableLine(
            [
                'proxy_pass',
                'Куда будет отправляться запрос (проксируемый сервер)',
                'Адрес (https://address:port).'
            ]
        ),
        ContentTableLine(
            [
                'proxy_set_header',
                'Задает заголовок http запроса, который будет отправлен проксируемому серверу',
                escape('<заголовок> <на что меняем>. Какие заголовки нужно менять, смотри ниже')
            ]
        )
    ]
)

proxy_uri = """http{
	server{
		listen 5001;
		location /usual_uri {
			proxy_pass http://127.0.0.1:5002;
		}
		location /without_backslash {
			proxy_pass http://127.0.0.1:5002/;
		}
		location /some/prefixes/etc {
		    proxy_pass http://127.0.0.1:5002/main_prefix/
		}
	}
	server{
		listen 5002;
		location / {root /home/seventwelve712/www/;}
	}
}"""

tls = ContentTable(
    False,
    ['Директива', 'За что отвечает', 'Значение'],
    [
        ContentTableLine(
            [
                'listen',
                'Надо дописать ssl после порта, чтобы сказать, что вебсервер работает с использованием шифрования',
                'port ssl'
            ]
        ),
        ContentTableLine(
            [
                'ssl_certificate',
                'Путь к ssl сертификату (публичный ключ)',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'ssl_certificate_key',
                'Путь к ключу сертификата (приватный ключ)',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'ssl_protocols',
                'Какие протоколы будут использоваться. На май 2025 считаются безопасными TLSv1.2 и TLSv1.3',
                'Протоколы через пробел'
            ]
        ),
        ContentTableLine(
            [
                'ssl_ciphers',
                'Какие шифры tls предложит клиенту. Рекомендуется использовать эти:',
                "'TLS_AES_256_GCM_SHA384:<br>TLS_CHACHA20_POLY1305_SHA256:<br>TLS_AES_128_GCM_SHA256:<br>ECDHE-ECDSA-AES256-GCM-SHA384:<br>ECDHE-RSA-AES256-GCM-SHA384'"
            ]
        ),
        ContentTableLine(
            [
                'ssl_prefer_<br>server_ciphers',
                'Делает шифры сервера предпочтительнее шифров клиента (если значение on)',
                'on/off'
            ]
        )
    ]
)

main_ex = """user www-data;
worker_processes 1;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
include /etc/nginx/modules-enabled/*.conf;"""

events_ex = """events {
	worker_connections 8192;
}"""

http_ex = """http{
    access_log /var/log/nginx/access.log;
    server {}
}"""

server_ex = """server{
    listen 80;
    server_name webreminder712.ru;
    return 301 https://webreminder712.ru:44344$request_uri;
    location / {}
}"""

location_ex1 = """location /some_data{
    root /var/www/data
}"""

proxy_ex = """location /{
    proxy_pass http://127.0.0.1:8000/;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Prefix /;
}"""

tls_ex = """server{
    listen 44344 ssl;
    server_name webreminder712.ru;
    ssl_certificate /home/seventwelve712/www/serts/cert;
    ssl_certificate_key /home/seventwelve712/www/serts/key;
    ssl_protocols TLSv1.3 TLSv1.2;
    ssl_ciphers 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256<br>:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;
    location / {}
}"""

mini = """events {}
http {
    server {
        listen 80;
    }
}"""

total = """user seventwelve712;
worker_processes 1;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 8192;
}
http {
	# Настраиваем логи доступа
	access_log /var/log/nginx/access.log;

	# Настраиваем редирект с http на https
	server{
		listen 80;
		server_name webreminder712.ru;
		return 301 https://webreminder712.ru:44344$request_uri;
	}

	# Сам http сервер
	server{
		listen 44344 ssl;
		server_name webreminder712.ru;

		# настройка tls соединения
		ssl_certificate /home/seventwelve712/www/serts/cert;
		ssl_certificate_key /home/seventwelve712/www/serts/key;
		ssl_protocols TLSv1.3 TLSv1.2;
		ssl_ciphers 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256<br>:TLS_AES_128_GCM_SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';
		ssl_prefer_server_ciphers on;

		# Настраиваем статусную страницу
		location /nginx_status{
			stub_status on;
			access_log off;
			# Разрешаем с локалхоста
			allow 127.0.0.1;
			# Запрещаем со всех остальных адресов
			deny all;
		}

		# Настраиваем перенаправление на внутренний сервер (гуникорн)
		location /{
			proxy_pass http://127.0.0.1:8000/;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_set_header X-Forwarded-Host $host;
			proxy_set_header X-Forwarded-Prefix /;
		}
	}
}
"""

location_status = """location /nginx_status{
    stub_status on;
    access_log off;
    allow 127.0.0.1;
    deny all;
}"""

kwargs = {
    "block_dir": block_dir,
    "main": main,
    "events": events,
    "http": http_,
    "server": server,
    "location_ex": location_ex,
    "location": location,
    "proxy_uri": proxy_uri,
    "proxy": proxy,
    "tls": tls,
    "main_ex": main_ex,
    "events_ex": events_ex,
    "http_ex": http_ex,
    "server_ex": server_ex,
    "location_ex1": location_ex1,
    "proxy_ex": proxy_ex,
    "tls_ex": tls_ex,
    "mini": mini,
    "total": total,
    "location_status": location_status
}
page = Instruction('nginx', 'nginx.html', kwargs, define_from_html('nginx.html'))
