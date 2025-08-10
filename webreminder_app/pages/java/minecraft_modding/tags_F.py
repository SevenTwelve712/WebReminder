from webreminder_app.utils.content_table import ContentTableLine, ContentTable
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/tags.html"
chapter_list = define_from_html(html_path)

vanilla_tags = ContentTable(
    caption=False,
    header=["тег", "за что отвечает"],
    lines=[
        # 🧱 Теги блоков
        ContentTableLine("🧱 Теги блоков (data/minecraft/tags/blocks/)", type_="subhead"),
        ContentTableLine(["mineable/pickaxe", "Можно добыть киркой"]),
        ContentTableLine(["mineable/axe", "Можно добыть топором"]),
        ContentTableLine(["mineable/shovel", "Можно добыть лопатой"]),
        ContentTableLine(["mineable/hoe", "Можно добыть мотыгой"]),
        ContentTableLine(["needs_stone_tool", "Требует минимум каменную кирку для добычи"]),
        ContentTableLine(["needs_iron_tool", "Требует железную или лучше"]),
        ContentTableLine(["needs_diamond_tool", "Требует алмазную или лучше"]),
        ContentTableLine(["leaves", "Листва деревьев"]),
        ContentTableLine(["logs", "Все виды бревен"]),
        ContentTableLine(["logs_that_burn", "Горящие бревна (топливо)"]),
        ContentTableLine(["planks", "Все доски"]),
        ContentTableLine(["sand", "Все виды песка"]),
        ContentTableLine(["flowers", "Все цветы"]),
        ContentTableLine(["saplings", "Все саженцы деревьев"]),
        ContentTableLine(["fences", "Заборы"]),
        ContentTableLine(["wool", "Все виды шерсти"]),
        ContentTableLine(["doors", "Все двери"]),
        ContentTableLine(["beds", "Все кровати"]),
        ContentTableLine(["ice", "Все виды льда"]),
        ContentTableLine(["snow", "Снег и снежные блоки"]),
        ContentTableLine(["rail", "Рельсы"]),
        ContentTableLine(["impermeable", "Блоки, через которые не проходят жидкости"]),
        ContentTableLine(["guarded_by_piglins", "Вещи, охраняемые пиглинами"]),

        # 🎒 Теги предметов
        ContentTableLine("🎒 Теги предметов (data/minecraft/tags/items/)", type_="subhead"),
        ContentTableLine(["logs", "Бревна всех видов"]),
        ContentTableLine(["planks", "Доски всех пород дерева"]),
        ContentTableLine(["sticks", "Палочки"]),
        ContentTableLine(["tools", "Все стандартные инструменты"]),
        ContentTableLine(["swords", "Все мечи"]),
        ContentTableLine(["axes", "Все топоры"]),
        ContentTableLine(["pickaxes", "Все кирки"]),
        ContentTableLine(["shovels", "Все лопаты"]),
        ContentTableLine(["hoes", "Все мотыги"]),
        ContentTableLine(["fishes", "Все виды рыбы"]),
        ContentTableLine(["arrows", "Все стрелы"]),
        ContentTableLine(["wool", "Все виды шерсти"]),
        ContentTableLine(["flowers", "Все цветы"]),
        ContentTableLine(["music_discs", "Музыкальные диски"]),
        ContentTableLine(["coals", "Уголь и древесный уголь"]),
        ContentTableLine(["lectern_books", "Книги, которые можно поставить на кафедру"]),
        ContentTableLine(["piglin_loved", "Предметы, которые нравятся пиглинам (например, золото)"]),
        ContentTableLine(["stone_crafting_materials", "Материалы для каменного крафта (камень, булыжник и т.п.)"]),

        # 👾 Теги существ
        ContentTableLine("👾 Теги существ (data/minecraft/tags/entity_types/)", type_="subhead"),
        ContentTableLine(["skeletons", "Все скелеты (обычные, визеры и т.п.)"]),
        ContentTableLine(["raiders", "Все участники рейдов"]),
        ContentTableLine(["beehive_inhabitors", "Пчёлы и связанные сущности"]),
        ContentTableLine(["powder_snow_walkable_mobs", "Существа, не проваливающиеся в снежную пудру"]),
        ContentTableLine(["axolotl_always_hostiles", "Кого всегда атакует аксолотль"]),
        ContentTableLine(["impact_projectiles", "Снаряды (стрелы, снежки, огненные шары)"]),
    ]
)

tag_create = "public static final TagKey<Block> TAG =\n    BlockTags.create(ResourceLocation.fromNamespaceAndPath(mod_id, tag_id));"

tags_json = '''{
  "replace": false или true, в зависимости от того, хотим ли мы заместить это файл,
  если forge найдет еще один с таким же id тега,
  "values": [
    "mod_id:item_id",
    "mod_id:block_id"
  ]
}'''

kwargs = {
    "tags_json": tags_json,
    "vanilla_tags": vanilla_tags,
    "tag_create": tag_create
}
instruction = Instruction(
    'Теги',
    html_path,
    kwargs,
    chapter_list
)
