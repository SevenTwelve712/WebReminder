from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/json_structure.html"
chapter_list = define_from_html(html_path)

structure = """src/
└── main/
    └── resources/
        ├── assets/
        │   └── <mod_id>/                  # 🔹 Все клиентские ресурсы для твоего мода
        │       ├── lang/                  # 🌐 Переводы (например, en_us.json, ru_ru.json)
        │       ├── models/
        │       │   ├── block/             # 🧱 Модели блоков
        │       │   └── item/              # 🎒 Модели предметов
        │       ├── blockstates/           # 🧩 BlockState JSON-файлы для блоков
        │       ├── textures/
        │       │   ├── block/             # 🖼️ Текстуры блоков
        │       │   └── item/              # 🖼️ Текстуры предметов
        │       └── sounds/                # 🔊 Кастомные звуки (если есть)
        │
        └── data/
            ├── minecraft/                # 🔁 Встроенные теги, рецепты vanilla и переопределения
            └── <mod_id>/                 # 🔸 Игровая логика и механики твоего мода
                ├── recipes/              # 🍲 Рецепты крафта (JSON)
                ├── loot_tables/          # 🎁 Дроп с блоков, мобов, сундуков
                │   ├── blocks/
                │   └── entities/
                ├── advancements/         # 🏆 Достижения
                ├── tags/
                │   ├── blocks/           # 🏷️ Теги блоков (например, "ores", "logs")
                │   ├── items/            # 🏷️ Теги предметов
                │   └── entity_types/     # 🏷️ Теги существ (если нужно)
                └── functions/            # 🧠 Командные функции"""

lang = '''{
    "item.mod_id.item_id": "translation",
    "block.mod_id.block_id": "translation",
    "creativetab.mod_id.creative_tab_id": "translation",
    "tooltips.mod_id.tooltip_id": "translation"
}'''

block_model = '''{
  "parent": "minecraft:block/cube_all",
  "textures": {
    "all": "mod_id:block/block_id"
  }
}'''

item_model = '''{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "mod_id:item/item_id"
  }
}'''

blockstates = '''{
  "variants": {
    "prop_id=val1": {
      "model": "mod_id:block/block_id_val1"
    },
    "prop_id=val2": {
      "model": "mod_id:block/block_id_val2"
    }
  }
}'''

recipy = '''{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "A": {
      "item": "mod_id:item_id"
    }
  },
  "pattern": [
    "AA ",
    "AA ",
    "   "
  ],
  "result": {
    "count": 1,
    "id": "mod_id:item_id"
  }
}'''

recipy_shapeless = '''{
  "type": "minecraft:crafting_shapeless",
  "ingredients": [
    { "item": "mod_id:item_id" },
    { "item": "mod_id:item_id" }
  ],
  "result": {
    "item": "mod_id:item_id",
    "count": 1
  }
}'''

tags = '''{
  "replace": false или true, в зависимости от того, хотим ли мы заместить это файл,
  если forge найдет еще один с таким же id тега,
  "values": [
    "mod_id:item_id",
    "mod_id:block_id"
  ]
}'''

kwargs = {
    'structure': structure,
    'lang': lang,
    'block_model': block_model,
    'item_model': item_model,
    'blockstates': blockstates,
    'recipy': recipy,
    'recipy_shapeless': recipy_shapeless,
    'tags': tags
}
instruction = Instruction(
    'Структура json файлов в проекте',
    html_path,
    kwargs,
    chapter_list
)
