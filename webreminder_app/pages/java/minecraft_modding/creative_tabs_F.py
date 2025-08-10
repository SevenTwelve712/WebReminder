from webreminder_app.utils.instruction import Instruction
from webreminder_app.utils.chapter_list import define_from_html

html_path = "/java/minecraft_modding/creative_tabs.html"
chapter_list = define_from_html(html_path)

creative_tabs_class = """public class ModCreativeModTabs {

    // Создаем реестр вкладок
    public static final DeferredRegister<CreativeModeTab> CREATIVE_MOD_TABS =
            DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MOD_ID);

    // Регистрируем реестр в моде
    public static void register(IEventBus eventBus){
        CREATIVE_MOD_TABS.register(eventBus);
    }
}"""

tabs_registration = """// Создаем са объект вкладки
public static final RegistryObject<CreativeModeTab> TAB = CREATIVE_MOD_TABS.register(
        "tab_id", () -> CreativeModeTab.builder()
                .withTabsBefore(TAB_.getId()) // Если нам надо, чтобы до этой вкладки шли еще какие-либо
                .icon(() -> new ItemStack(ModBlocks.SEVEN_BLOCK.get())) // создаем иконку
                .title(Component.translatable("title_id, потом не забываем его перевести в lang"))
                .displayItems((itemDisplayParameters, output) -> {
                    output.accept(здесь добавляем наши предметы);
                })
                .build()
);"""

kwargs = {
    'creative_tabs_class': creative_tabs_class,
    'tabs_registration': tabs_registration
}
instruction = Instruction(
    'Создание вкладок в инвентаре креатива',
    html_path,
    kwargs,
    chapter_list
)
