from webreminder_app.utils.content_table import ContentTable, ContentTableLine
from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/block.html"
chapter_list = define_from_html(html_path)

block_classes = ContentTable(
    caption=False,
    header=['Блок', 'аргументы', 'когда используется'],
    lines=[
        ContentTableLine(['Block(Properties)', 'Properties — базовые свойства блока', 'Обычный статичный блок без особого поведения']),
        ContentTableLine(['DropExperienceBlock(Properties, expAmount)', 'Properties — свойства блока, expAmount — диапазон опыта (например, UniformInt.of(1, 3))', 'Для руд и других блоков, дропающих опыт при разрушении']),
        ContentTableLine(['FallingBlock(Properties)', 'Properties — свойства блока', 'Падающий блок, если под ним воздух (например, песок, гравий)']),
        ContentTableLine(['RotatedPillarBlock(Properties)', 'Properties — свойства блока', 'Вертикальные или горизонтальные брёвна, колонны и т.п.']),
        ContentTableLine(['SlabBlock(Properties)', 'Properties — свойства блока', 'Плиты — половинный блок по высоте']),
        ContentTableLine(['StairBlock(baseState, Properties)', 'baseState — состояние базового блока, Properties — свойства лестницы', 'Для лестниц, повторяющих внешний вид другого блока']),
        ContentTableLine(['WallBlock(Properties)', 'Properties — свойства блока', 'Блоки-стены, соединяются с другими блоками по сторонам']),
        ContentTableLine(['ButtonBlock(ticks, blockSetType, canBePressedByArrow, Properties)', 'ticks — время нажатия, blockSetType — тип кнопки, canBePressedByArrow — можно ли стрелой', 'Кнопки, подающие сигнал Redstone']),
        ContentTableLine(['PressurePlateBlock(sensitivity, blockSetType, Properties)', 'sensitivity — что активирует плиту (всё/мобы/игрок), blockSetType, Properties', 'Нажимные плиты']),
        ContentTableLine(['LeverBlock(Properties)', 'Properties — свойства блока', 'Простые переключатели Redstone']),
        ContentTableLine(['TorchBlock(Properties, particleType)', 'Properties — свойства, particleType — частицы (обычно пламя)', 'Статичный источник света']),
        ContentTableLine(['WallTorchBlock(Properties, particleType)', 'Properties, particleType — как у TorchBlock', 'Факел, крепящийся на стены']),
        ContentTableLine(['RedstoneTorchBlock(Properties)', 'Properties — свойства блока', 'Источник постоянного Redstone-сигнала']),
        ContentTableLine(['FlowerBlock(effect, duration, Properties)', 'effect — эффект зелья, duration — длительность, Properties', 'Цветы, дающие эффект при еде']),
        ContentTableLine(['BushBlock(Properties)', 'Properties — свойства блока', 'Маленькие декоративные растения']),
        ContentTableLine(['CropBlock(Properties)', 'Properties — свойства блока', 'Растения, которые растут стадиями (пшеница, морковь и т.п.)']),
        ContentTableLine(['LiquidBlock(fluid, Properties)', 'fluid — твой FlowingFluid, Properties — свойства блока', 'Кастомные жидкости (например, нефть, кислота)']),
        ContentTableLine(['DoorBlock(blockSetType, Properties)', 'blockSetType — тип двери (звук, поведение), Properties', 'Двухблочные двери']),
        ContentTableLine(['TrapDoorBlock(blockSetType, Properties)', 'blockSetType, Properties', 'Люки']),
        ContentTableLine(['FenceBlock(Properties)', 'Properties — свойства блока', 'Заборы, соединяющиеся с соседними блоками']),
        ContentTableLine(['FenceGateBlock(Properties, woodType)', 'Properties, woodType — тип дерева', 'Ворота между заборами']),
        ContentTableLine(['BedBlock(color, Properties)', 'color — цвет кровати (DyeColor), Properties', 'Кровати, занимают 2 блока, можно спать']),
    ]
)

properties = ContentTable(
    caption=False,
    header=['Свойство (с аргументами)', 'Аргументы', 'Что делает'],
    lines=[
        ContentTableLine(['.strength(float)', 'float: твёрдость блока (обычно 0.5–50.0)', 'Определяет, сколько времени нужно, чтобы разрушить блок']),
        ContentTableLine(['.strength(float, float)', 'float — прочность, float — взрывоустойчивость', 'Первая задаёт твёрдость, вторая — устойчивость к взрывам']),
        ContentTableLine(['.noOcclusion()', '—', 'Делает блок неполным — не мешает обзору и свету (например, забор)']),
        ContentTableLine(['.sound(SoundType)', 'SoundType: тип звуков (STONE, WOOD, GLASS и т.д.)', 'Определяет звук при разрушении, установке, шаге']),
        ContentTableLine(['.lightLevel(state -> int)', 'функция от BlockState, возвращает уровень света 0–15', 'Заставляет блок светиться']),
        ContentTableLine(['.requiresCorrectToolForDrops()', '—', 'Требует правильный инструмент (например, железную кирку)']),
        ContentTableLine(['.instabreak()', '—', 'Блок ломается мгновенно']),
        ContentTableLine(['.friction(float)', 'float: коэффициент трения (0.0–1.0, по умолчанию 0.6)', 'Влияет на скольжение игрока или моба по блоку']),
        ContentTableLine(['.jumpFactor(float)', 'float: множитель прыжка', 'Увеличивает (или уменьшает) высоту прыжка на этом блоке']),
        ContentTableLine(['.speedFactor(float)', 'float: множитель скорости движения', 'Меняет скорость игрока/моба на этом блоке']),
        ContentTableLine(['.noLootTable()', '—', 'Отключает дроп блока при разрушении']),
        ContentTableLine(['.isRedstoneConductor((state, world, pos) -> boolean)', 'функция, возвращает true/false', 'Определяет, проводит ли блок редстоун-сигнал']),
        ContentTableLine(['.explosionResistance(float)', 'float: устойчивость к взрывам', 'Только устойчивость, без влияния на скорость разрушения']),
        ContentTableLine(['.mapColor(MapColor)', 'MapColor: цвет на карте', 'Определяет цвет блока на карте (не текстура)']),
        ContentTableLine(['.randomTicks()', '—', 'Включает randomTick — используется для роста, плавления и т.п.']),
        ContentTableLine(['.offsetType(OffsetType)', 'OffsetType: NONE, XZ, XYZ', 'Смещает рендер модели блока случайно (например, цветы)']),
        ContentTableLine(['.dynamicShape()', '—', 'Говорит Minecraft, что форма блока зависит от его состояния']),
    ]
)

custom_block = """public class CustomBlock extends Block {
    CustomBlock(BlockBehaviour.Properties properties){
        super(properties);
    }
}"""

get_block_info = ContentTable(
    caption=False,
    header=['Метод', 'Что возвращает'],
    lines=[
        ContentTableLine(['getName()', 'локализованное имя блока (через регистр)']),
        ContentTableLine(['defaultBlockState()', 'базовое состояние (без изменений)']),
        ContentTableLine(['getStateDefinition()', 'описание всех возможных свойств блока']),
        ContentTableLine(['getSoundType(BlockState)', 'звук при взаимодействии']),
        ContentTableLine(['getDrops(BlockState, LootContext)', 'предметы, которые дропаются при разрушении']),
        ContentTableLine(['getLightEmission(BlockState)', 'сколько светит блок']),
        ContentTableLine(['getMaterial(BlockState)', 'материал блока (камень, дерево и т.п.)']),
        ContentTableLine(['hasTileEntity(BlockState)', 'есть ли у блока связанный BlockEntity']),
        ContentTableLine(['getRenderShape(BlockState)', 'форма блока для рендера (куб, модель и т.п.)']),
        ContentTableLine(['getCollisionShape(BlockState, BlockGetter, BlockPos)', 'форма коллизии']),
        ContentTableLine(['getLightBlock(BlockState, BlockGetter, BlockPos)', 'насколько блок блокирует свет']),
    ]
)

BlockStatesMethods = ContentTable(
    caption=False,
    header=['метод', 'что делает'],
    lines=[
        ContentTableLine(['getBlock()', 'Возвращает объект Block, из которого получено это состояние']),
        ContentTableLine(['getValue(Property<T>)', 'Получает значение конкретного свойства']),
        ContentTableLine(['hasProperty(Property<?>)', 'Проверяет, есть ли у блока такое свойство']),
        ContentTableLine(['getProperties()', 'Возвращает все Property<?>, зарегистрированные у блока']),
        ContentTableLine(['is(Block)', 'Проверяет, соответствует ли состояние конкретному типу блока']),
        ContentTableLine(['isAir()', 'Является ли состояние блоком воздуха']),
        ContentTableLine(['isSolidRender(BlockGetter, BlockPos)', 'Видит ли мир это состояние как непрозрачный блок']),
        ContentTableLine(['isCollisionShapeFullBlock(BlockGetter, BlockPos)', 'Полный ли у блока hitbox']),
        ContentTableLine(['getCollisionShape(BlockGetter, BlockPos)', 'Возвращает VoxelShape — форму столкновения (например, плиты, люки)']),
        ContentTableLine(['getRenderShape()', 'Тип рендера: MODEL, INVISIBLE, ENTITYBLOCK_ANIMATED и т.п.']),
        ContentTableLine(['getLightEmission()', 'Сколько света излучает блок (0–15)']),
        ContentTableLine(['getSoundType()', 'Возвращает SoundType (звук при разрушении, установке и т.д.)']),
        ContentTableLine(['getDestroySpeed(BlockGetter, BlockPos)', 'Насколько быстро разрушается блок']),
        ContentTableLine(['isRedstoneConductor(BlockGetter, BlockPos)', 'Проводит ли блок редстоун сигнал']),
    ]
)

property_registration = """@Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> pBuilder) {
        pBuilder.add(PROPERTY_NAME);
    }"""

blockstates_example = """{
  "variants": {
    "property_id=false": {
      "model": "my_mod:block/model_false"
    },
    "property_id=true": {
      "model": "my_mod:block/model_true"
    }
  }
}"""

block_model = """{
  "parent": "minecraft:block/cube_all",
  "textures": {
    "all": "my_mod:block/my_texture"
  }
}"""

kwargs = {
    'block_classes': block_classes,
    'properties': properties,
    'custom_block': custom_block,
    'get_block_info': get_block_info,
    'BlockStateMethods': BlockStatesMethods,
    'property_registration': property_registration,
    'blockstates_example': blockstates_example,
    'block_model': block_model
}
instruction = Instruction(
    'Блоки',
    html_path,
    kwargs,
    chapter_list
)
