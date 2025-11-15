from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html


cheatsheet = ContentTable(
    caption=False,
    header=["Команда", "Что делает"],
    lines=[
        # --- Инициализация ---
        ContentTableLine("Инициализация", type_="subhead"),
        ContentTableLine(["git init", "Создаёт новый локальный репозиторий"]),
        ContentTableLine(["git clone <url>", "Клонирует удалённый репозиторий"]),

        # --- Управление файлами ---
        ContentTableLine("Управление файлами", type_="subhead"),
        ContentTableLine(["git add <файл>", "Добавляет файл в индекс"]),
        ContentTableLine(["git rm <файл>", "Удаляет файл из индекса и рабочей директории"]),
        ContentTableLine(["git rm --cached <файл>", "Удаляет файл из индекса"]),
        ContentTableLine(["git mv <старое имя> <новое имя>", "Переименовывает или перемещает файл"]),
        ContentTableLine(["git restore file", "Возвращает файл в состояние предыдущего коммита (в рабочей директории)"]),
        ContentTableLine(["git restore --staged file", "Удаляет файл из индекса"]),
        ContentTableLine(["git restore --source <commit> file", "Восстанавливает файл из определенного коммита"]),
        ContentTableLine(["git restore --source branch", "Восстанавливает файл из заданной ветки"]),

        # --- Коммиты ---
        ContentTableLine("Коммиты", type_="subhead"),
        ContentTableLine(["git commit -m 'сообщение'", "Создаёт новый коммит"]),
        ContentTableLine(["git commit -am 'сообщение'", "Создаёт новый коммит, в который включены все измененные файлы"]),

        # --- Ветки ---
        ContentTableLine("Ветки", type_="subhead"),
        ContentTableLine(["git branch -vv", "Показывает список веток и информацию о них"]),
        ContentTableLine(["git branch <имя>", "Создаёт новую ветку"]),
        ContentTableLine(["git switch -b branch", "Создает новую ветку и сразу же переключается на нее"]),
        ContentTableLine(["git switch <ветка>", "Переключается на указанную ветку"]),
        ContentTableLine(["git branch -d branch", "Удаляет ветку"]),
        ContentTableLine(["git merge <ветка>", "Сливает указанную ветку в текущую"]),
        ContentTableLine(["git rebase <ветка>", "Перебазирует указанную ветку в текущую"]),
        ContentTableLine(["git merge", "Сливает ветку и ее удаленный аналог, если изменения получены с сервера"]),

        # --- Истоия ---
        ContentTableLine(["git log", "Показывает историю коммитов"]),
        ContentTableLine(["git log branch", "Показывает историю коммитов ветки"]),
        ContentTableLine(["git log --graph", "Показывает историю коммитов в виде графа"]),
        ContentTableLine(["git log --oneline", "Показывает историю коммитов в сокращенном виде"]),
        ContentTableLine(["git diff", "Показывает изменения между коммитами или рабочими файлами"]),
        ContentTableLine(["git status", "Показывает состояние файлов и индекса"]),

        # --- Удалённые репозитории ---
        ContentTableLine("Удалённые репозитории", type_="subhead"),
        ContentTableLine(["git remote -v", "Показывает список удалённых репозиториев"]),
        ContentTableLine(["git remote add <имя> <url>", "Добавляет удалённый репозиторий"]),
        ContentTableLine(["git fetch", "Загружает изменения из удалённого репозитория без слияния"]),
        ContentTableLine(["git push -u origin main", "Пушит изменения ветки main на сервер origin, привязывая ее к одноименной удаленной ветке"]),
        ContentTableLine(["git push origin main", "Пушит изменения в репозиторий origin на ветку main"]),
        ContentTableLine(["git push", "Пушит изменения ветки в ее удаленный аналог"]),
        ContentTableLine(["git pull origin main", "Загружает и сливает изменения с ветки origin/main"]),
        ContentTableLine(["git pull", "Загружает и сливает изменения с привязанной удаленной ветки"]),
    ]
)
html = 'instructions/git.html'
chapter_list = define_from_html(html)
kwargs = {
    "cheatsheet": cheatsheet
}
page = Instruction(
    'git',
    html,
    kwargs,
    chapter_list
)
