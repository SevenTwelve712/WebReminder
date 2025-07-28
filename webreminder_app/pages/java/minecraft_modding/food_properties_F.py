from webreminder_app.utils.content_table import *
from webreminder_app.utils.table_only import TableOnlyPage

extra = 'Для создания нового свойства делаем: <code>public static final FoodProperties PROPERTY = ' \
        'new FoodProperties.Builder().properties(...)</code>'

content = ContentTable(
    'FoodProperties',
    header=['Свойство', 'Аргументы', 'Что делает'],
    lines=[
        ContentTableLine(['nutrition(int amount)', 'amount — сколько единиц голода восстанавливается (1 ед. = 0.5 "бедрышка")', 'Устанавливает, сколько голода восстанавливает еда']),
        ContentTableLine(['saturationMod(float amount)', 'amount — множитель насыщения (от 0.0 до ~1.0)', 'Устанавливает уровень насыщения: чем выше, тем дольше игрок остаётся сытым']),
        ContentTableLine(['alwaysEat()', '—', 'Позволяет есть еду даже если игрок полностью сыт']),
        ContentTableLine(['fast()', '—', 'Делает еду быстрой в поедании (анимация занимает 15 тиков вместо 32)']),
        ContentTableLine(['meat()', '—', 'Помечает еду как мясо — животные (например, волки) смогут её есть']),
        ContentTableLine([
            'effect(() -> new MobEffectInstance(effect, duration, amplifier), float probability)',
            'effect — добавляемый эффект\nduration — длительность в тиках\namplifier — уровень эффекта\nprobability — шанс от 0.0 до 1.0',
            'Добавляет специальный эффект на игрока при поедании с заданной вероятностью'
        ]),
    ]
)
page = TableOnlyPage('FoodProperties', extra, content)
