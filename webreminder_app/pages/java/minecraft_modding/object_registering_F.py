from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/object_registering.html"
chapter_list = define_from_html(html_path)

block_reg = """public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS,
        SevenMod.MODID);

public static final RegistryObject<Block> SEVEN_BLOCK = registerBlock("seven_block",
        () -> new Block(BlockBehaviour.Properties.of()));
    
BLOCKS.register(modEventBus);"""

kwargs = {
    'block_reg':  block_reg
}
instruction = Instruction(
    'Регистрация объектов',
    html_path,
    kwargs,
    chapter_list
)
