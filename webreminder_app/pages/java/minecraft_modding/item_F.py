from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/item.html"
chapter_list = define_from_html(html_path)

properties = ContentTable(
    caption=False,
    header=['Property', 'за что отвечает'],
    lines=[
        ContentTableLine(['.durability(int)', 'Прочность предмета (если инструмент)']),
        ContentTableLine(['.food(FoodProperties)', 'Указывает, что предмет съедобный ']),
        ContentTableLine(['.rarity(Rarity.EPIC)', 'Редкость: COMMON, UNCOMMON, RARE, EPIC']),
        ContentTableLine(['.stacksTo(16)', 'Максимальное количество в стаке (по умолчанию 64)']),
        ContentTableLine(['.fireResistant()', 'Предмет не сгорает в лаве или огне']),
        ContentTableLine(['.craftRemainder(Items.BUCKET)', 'Что остаётся после крафта']),
        ContentTableLine(['.defaultDurability(100)', 'Прочность по умолчанию (при создании)']),
        ContentTableLine(['.arch$tab(CreativeModeTabs.TOOLS_AND_UTILITIES)', 'Назначение вкладки в креативе (новый Forge)']),
    ]
)

custom_item = """public class MagicWandItem extends Item {
    public MagicWandItem(Properties properties){
        super(properties);
    }
}"""

UseOnContext = ContentTable(
    caption=False,
    header=['Метод', 'Что делает'],
    lines=[
        ContentTableLine(['getLevel()', 'Возвращает Level (мир), в котором был использован предмет']),
        ContentTableLine(['getPlayer()', 'Возвращает Player, который использует предмет, или null, если игрока нет (например, при использовании от имени командного блока)']),
        ContentTableLine(['getHand()', 'Возвращает InteractionHand (MAIN_HAND или OFF_HAND), то есть в какой руке предмет']),
        ContentTableLine(['getItemInHand()', 'Возвращает ItemStack, которым щёлкнули (предмет в руке)']),
        ContentTableLine(['getClickedPos()', 'Возвращает BlockPos блока, по которому кликнули']),
        ContentTableLine(['getClickedFace()', 'Возвращает Direction (сторона блока, по которой кликнули: UP, DOWN, NORTH и т.д.)']),
        ContentTableLine(['getClickedBlockState()', 'Возвращает BlockState блока, по которому кликнули']),
        ContentTableLine(['getClickLocation()', 'Возвращает Vec3 – точную позицию клика по блоку в мире (например, для ray tracing)']),
        ContentTableLine(['getHorizontalDirection()', 'Направление, куда смотрит игрок по горизонтали']),
        ContentTableLine(['isInside()', 'Возвращает true, если клик был внутри границ блока (полезно при взаимодействии с блоками, имеющими неполный хитбокс)']),
    ]
)

item_itemstack = ContentTable(
    caption=False,
    header=['метод', 'что делает'],
    lines=[
        ContentTableLine('Item', type_='subhead'),
        ContentTableLine(['getDefaultInstance()', 'Возвращает стандартный ItemStack этого предмета (используется, например, для иконки в креативке)']),
        ContentTableLine(['isEnchantable(ItemStack)', 'Возвращает, можно ли зачаровать предмет']),
        ContentTableLine(['getMaxStackSize()', 'Максимальное количество предметов в стаке']),
        ContentTableLine(['getMaxDamage()', 'Возвращает максимальную прочность предмета (если применимо)']),
        ContentTableLine(['isDamageable(ItemStack)', 'Возвращает true, если у предмета есть прочность']),
        ContentTableLine(['getUseDuration(ItemStack)', 'Сколько тиков занимает использование предмета (например, 32 тика у еды)']),
        ContentTableLine(['getUseAnimation(ItemStack)', 'Тип анимации при использовании (EAT, DRINK, BLOCK, BOW и др.)']),
        ContentTableLine(['isFoil(ItemStack)', 'Показывает, мигает ли предмет (например, зачарованный)']),
        ContentTableLine(['canBeDepleted()', 'Возвращает true, если у предмета ограниченная прочность']),
        ContentTableLine(['isRepairable(ItemStack)', 'Можно ли чинить предмет']),

        ContentTableLine('ItemStack', type_='subhead'),
        ContentTableLine(['getItem()', 'Возвращает объект Item, которому принадлежит этот стак']),
        ContentTableLine(['getDamageValue() / setDamageValue(int)', 'Получение/установка текущего урона предмета']),
        ContentTableLine(['hurtAndBreak(int amount, LivingEntity, Consumer)', 'Наносит урон предмету, ломает, вызывает callback']),
        ContentTableLine(['isEmpty()', 'Проверка, пуст ли стак']),
        ContentTableLine(['is(Item)', 'Проверка, является ли этот стак конкретным предметом']),
        ContentTableLine(['getTag() / setTag(CompoundTag)', 'Получение или установка NBT-данных']),
        ContentTableLine(['hasTag()', 'Есть ли у предмета NBT-данные']),
        ContentTableLine(['copy()', 'Создаёт копию ItemStack (очень полезно при клонировании или модификации)']),
        ContentTableLine(['enchant(Enchantment, int)', 'Применяет чары к предмету (программно)']),
        ContentTableLine(['isEnchanted()', 'Есть ли чары у предмета']),
        ContentTableLine(['setHoverName(Component)', 'Устанавливает пользовательское имя предмета']),
        ContentTableLine(['hasCustomHoverName() / getHoverName()', 'Проверка на пользовательское имя и его получение']),
        ContentTableLine(['shrink(int) / grow(int)', 'Уменьшает/увеличивает размер стака']),
    ]
)

item_model = """{
  "parent": "minecraft:item/generated",
  "textures":{
    "layer0": "mod_id:item/item_id"
  }
}"""

kwargs = {
    'properties': properties,
    'custom_item': custom_item,
    'UseOnContext': UseOnContext,
    'item_itemstack': item_itemstack,
    'item_model': item_model
}
instruction = Instruction(
    'Предеты в майнкрафт',
    html_path,
    kwargs,
    chapter_list
)
