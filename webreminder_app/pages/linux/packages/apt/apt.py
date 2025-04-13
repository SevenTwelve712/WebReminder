from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.content_table import *
from webreminder_app.utils.unordered_list import UnorderedList
from webreminder_app.utils.chapter_list import define_from_html

commands_table = ContentTable(
    False,
    ['Команда', 'Что делает', 'Примечания'],
    [
        ContentTableLine(
            [
                'update',
                'Загружает новейшую информацию о пакетах (такую как завизимости, наличие обновлений итп) '
                'из репозиториев, но не апгрейдит их',
                ''
            ]
        ),
        ContentTableLine(
            [
                'upgrade',
                'Устанавливает апгрейды пакетов. Никогда не удаляет существующие пакеты, может только устанавливать новые '
                '(если этого требуют зависимости)',
                'Имеет смысл использовать после apt update'
            ]
        ),
        ContentTableLine(
            [
                'full-upgrade',
                'То же самое, что и апгрейд, но может удалять пакеты, если это требуется для апгрейда системы в целом',
                ''
            ]
        ),
        ContentTableLine(
            [
                'install',
                'Устанавливает пакет',
                ''
            ]
        ),
        ContentTableLine(
            [
                'reinstall',
                'Переустанавливает пакет',
                ''
            ]
        ),
        ContentTableLine(
            [
                'remove',
                'Удаляет пакет, но сохраняет пользовательские конфиги (на случай, если удаление произошло случайно)',
                ''
            ]
        ),
        ContentTableLine(
            [
                'purge',
                'Полностью удаляет пакет, вместе с пользовательскими конфигами',
                ''
            ]
        ),
        ContentTableLine(
            [
                'autoremove',
                'Удалит пакеты, которые были автоматически установлены для удовлетворения потребностей других пакетов, '
                'и ненужные теперь',
                ''
            ]
        ),
        ContentTableLine(
            [
                'satisfy',
                'Удовлетворяет потребности пакетов, еще может решать конфликты',
                'Читай man для более подробной информации',
            ]
        ),
        ContentTableLine(
            [
                'search',
                'Ищет что-либо среди имен доступных пакетов, может работать с регулярными выражениями',
                ''
            ]
        ),
        ContentTableLine(
            [
                'show',
                'Показывает информацию о пакете',
                ''
            ]
        ),
        ContentTableLine(
            [
                'list',
                'Показывает список пакетов по определенным правилам',
                UnorderedList(['--installed покажет список установленных пакетов',
                               '--upgradeable покажет список пакетов пакетов, которые можно проапгрейдить',
                               '--all-versions покажет список всех пакетов с версиями'])
            ]
        )
    ]
)
sources = """deb https://deb.debian.org/debian bookworm main non-free-firmware
deb-src https://deb.debian.org/debian bookworm main non-free-firmware

deb https://security.debian.org/debian-security bookworm-security main non-free-firmware
deb-src https://security.debian.org/debian-security bookworm-security main non-free-firmware

deb https://deb.debian.org/debian bookworm-updates main non-free-firmware
deb-src https://deb.debian.org/debian bookworm-updates main non-free-firmware"""
kwargs = {
    'commands_table':commands_table,
    'sources': sources
}
page = Instruction('apt', 'apt.html', kwargs, define_from_html('apt.html'))
