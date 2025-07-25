from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/entry_point.html"
chapter_list = define_from_html(html_path)

entry_point_ex = """@Mod(SevenMod.MODID)
public class SevenMod{
   public static final String MODID = "sevenmod";
}
    public SevenMod(FMLJavaModLoadingContext context){
        IEventBus modEventBus = context.getModEventBus();
        MinecraftForge.EVENT_BUS.register(this);
    }"""

kwargs = {
    'entry_point_ex': entry_point_ex
}
instruction = Instruction(
    'Входная точка и настройки мода',
    html_path,
    kwargs,
    chapter_list
)
