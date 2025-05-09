from webreminder_app.utils.content_table import *
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

sshd_configs = ContentTable(
    False,
    ['Поле', 'За что отвечает', 'Что вписывать'],
    [
        ContentTableLine(
            [
                'Port',
                'На каком порту ssh будет слушать подключение',
                'Цифра'
            ]
        ),
        ContentTableLine(
            [
                'SyslogFacility',
                'Задает правило логирования (по ходу, какие типы сообщений будут логироваться, но не точно)',
                'Фиксированные значения, возможные варианты смотри в man, по дефолту стоит AUTH'
            ]
        ),
        ContentTableLine(
            [
                'LogLevel',
                'Задает уровень логирования. Например, если уровень логирования FATAL, то сообщения о парсинге '
                'ключа выводиться не будут',
                'Фиксированные значения'
            ]
        ),
        ContentTableLine(
            [
                'PermitRootLogin',
                'Разрешает вход по руту (надо запретить, по соображениям безопасности)',
                'yes/no'
            ]
        ),
        ContentTableLine(
            [
                'PubkeyAuthentication',
                'Разрешает вход по ключу',
                'yes/no'
            ]
        ),
        ContentTableLine(
            [
                'AuthorizedKeysFile',
                'Задает путь к публичным ключам, по которым будет производиться идентефикация',
                'Путь'
            ]
        ),
        ContentTableLine(
            [
                'PasswordAuthentication',
                'Разрешает соединение по паролю',
                'yes/no'
            ]
        ),
        ContentTableLine(
            [
                'PermitEmptyPassword',
                'Разрешить пустой пароль (нужно запретить)',
                'yes/no'
            ]
        ),
    ]
)

ssh_keygen = ContentTable(
    False,
    ['Параметр', 'За что отвечает', 'Какие значения принимает'],
    [
        ContentTableLine([
            '-m',
            'Формат, в котором будут создаваться ключи',
            'Я знаю только про PEM'
        ]),
        ContentTableLine([
            '-t',
            'Тип ключей',
            'rsa, ed25519'
        ]),
        ContentTableLine([
            '-b',
            'Количество бит в ключе, рекомендуется 4096',
            'Число'
        ]),
        ContentTableLine([
            'C',
            'Комментарий, который будет добавлен в конце файла открытого ключа. Можно добавлять любой, обычно пишут свою электронную почту',
            'Строка'
        ]),
        ContentTableLine([
            '-f',
            'Имя файла закрытого ключа. В той же директории создастся файл с расширением .pub: это публичный ключ',
            'Путь'
        ]),
        ContentTableLine([
            '-N',
            'Дополнительная парольная фраза, используемая для доступа к файлу закрытого ключа.',
            'Любая строка'
        ])
    ]
)
kwargs = {'sshd_configs': sshd_configs, 'ssh_keygen': ssh_keygen}
page = Instruction('ssh', 'ssh.html', kwargs, define_from_html('ssh.html'))
