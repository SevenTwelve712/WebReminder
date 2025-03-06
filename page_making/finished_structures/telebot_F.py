from page_making.classes.instructions import *
from help.support.abspaths import static_pages
from pathlib import Path

code1 = """from telebot import *

bot = TeleBot('Token')
bot.infinity_polling()"""

code2 = """bot.send_message(message.chat.id, 'text')
# message.chat.id всего лишь пример переменной, так то нужен конкретный chatid"""

code3 = """bot.reply_to(message, text='text')
# message всего лишь пример переменной, так то нужно конкретное сообщение
# (внимание, не chatid, а именно сообщение)"""

code4 = """bot.send_photo(message.chat.id, open("C:\\Users\\seven\\Pictures\\Идеи для обоев\\6.jpg", 'rb'))
# bot.send_photo(chatid, open('Путь к файлу', 'rb'))
# Не сжатое фото"""

code5 = """bot.send_video(message.chat.id, open("C:\\Users\\seven\\Pictures\\1.mp4", 'rb'))
# bot.send_video(chatid, open('Путь к файлу', 'rb'))
# Не сжатое видео"""

code6 = """bot.send_audio(message.chat.id, open("C:\\Users\\seven\\Pictures\\Временка\\1.mp3", 'rb'))
# bot.send_audio(chatid, open('Путь к файлу', 'rb'))"""

code7 = """bot.send_document(message.chat.id, open("C:\\Users\\seven\\Pictures\\Временка\\1.ttf", 'rb'))
# bot.send_audio(chatid, open('Путь к файлу', 'rb'))
# если таким образом отправить изображение оно будет сжатым, но если отправить видео,
# оно будет не сжатым"""

code8 = """@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Пошел нахуй")
# Данный код отправит тому, кто запустил бота (автоматически отправляется команда /start)
# сообщение "Пошел нахуй"""

code9 = """@bot.message_handler(content_types=["text"])
def text_replyer(message):
    if message.text == 'Иди нахуй':
        bot.send_message(message.chat.id, "Сам нахуй иди шалава ебаная")
# Данный код отправит тому еблану, кто написал "Иди нахуй"
# сообщение "Сам нахуй иди шалава ебаная"""

code10 = """@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b1 = types.KeyboardButton(text="Suck dick")
    b2 = types.KeyboardButton(text="Fuck ass")
    b3 = types.KeyboardButton(text="Suction")
    b4 = types.KeyboardButton(text="Billy")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Fuck you', reply_markup=markup)
# Данный код по команде \start отправит сообщение Fuck you пользователю, + у юзера появится поле
# с кнопками Suck dick, Fuck ass, Suction, Billy"""

code11 = """@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton(text="Suck dick", callback_data="gachi1")
    b2 = types.InlineKeyboardButton(text="Fuck ass", callback_data="gachi2")
    b3 = types.InlineKeyboardButton(text="Suction", callback_data="gachi3")
    b4 = types.InlineKeyboardButton(text="Billy", callback_data="gachi4")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Fuck you', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "gachi1":
            bot.send_message(call.message.chat.id, "Without further interraption")
        elif call.data == "gachi2":
            bot.send_message(call.message.chat.id, "AAAAAAAAA")
        if call.data == "gachi3":
            bot.send_message(call.message.chat.id, "6 hot loads")
        if call.data == "gachi4":
            bot.send_message(call.message.chat.id, "Herrington")


# Данный код по команде \start отправит сообщение Fuck you пользователю, под которым будет 4 кнопки,
# на которых будет написано Suck dick, Fuck ass, Suction, Billy.
# При нажатии на Suck dick юзеру отправится сообщение Without further interraption
# При нажатии на Fuck ass юзеру отправится сообщение AAAAAAAAA
# При нажатии на Suction юзеру отправится сообщение 6 hot loads
# При нажатии на Billy юзеру отправится сообщение Herrington"""

chapter_list = {
    'Начало': 'start',
    'Отправка сообщений': 'common_things',
    'Обработка команд': 'command_handler',
    'Обработка текста': 'text_handler',
    'Создание reply кнопок': 'replybutton_creating',
    'Создание inline кнопок': 'inlinebutton_creating'
}

content = [
    InstructionContentElem('h2', ['Начало работы с ботом', 'start']),
    InstructionContentElem('p', 'Что нужно для старта бота:'),
    InstructionContentElem('start_ul', None),
    InstructionContentElem('li', 'Создать объект бота, в котором указать токен'),
    InstructionContentElem('li', 'Запустить бота через метод infinity_polling()'),
    InstructionContentElem('end_ul', None),
    InstructionContentElem('p', 'Данный бот ничего не будет делать'),
    InstructionContentElem('code', code1),
    InstructionContentElem('h2', ['Отправка сообщений', 'common_things']),
    InstructionContentElem('p', 'Отправка сообщений обычным способом:'),
    InstructionContentElem('code', code2),
    InstructionContentElem('p', 'Ответ на сообщение:'),
    InstructionContentElem('code', code3),
    InstructionContentElem('p', 'Отправка фото:'),
    InstructionContentElem('code', code4),
    InstructionContentElem('p', 'Отправка видео:'),
    InstructionContentElem('code', code5),
    InstructionContentElem('p', 'Отправка аудио:'),
    InstructionContentElem('code', code6),
    InstructionContentElem('p', 'Отправка файла:'),
    InstructionContentElem('code', code7),
    InstructionContentElem('h2', ['Обработка команд', 'command_handler']),
    InstructionContentElem('p', 'Для обработки команд надо написать функцию, задекорировав ее декоратором @bot.message_handler с параметром commands=[Список команд]'),
    InstructionContentElem('code', code8),
    InstructionContentElem('h2', ['Обработка текста', 'text_handler']),
    InstructionContentElem('p', 'Для обработки текста надо написать функцию, задекрорировав ее декоратором @bot.message_handler с параметром content_types=["text"]'),
    InstructionContentElem('code', code9),
    InstructionContentElem('h2', ['Создание reply кнопок', 'replybutton_creating']),
    InstructionContentElem('p', 'Reply кнопки — кнопки, при нажатии которых в чат отсылается некий текст Для создания reply кнопок надо:'),
    InstructionContentElem('start_ul', None),
    InstructionContentElem('li', 'Создать объект types.ReplyKeyboardMarkup(row_width=кол-во сообщений в одном ряду, resize_keyboard=True)<br>Прим: параметр resize_keyboard нужно установить True если мы не хотим ебейшие кнопки на полэкрана'),
    InstructionContentElem('li', 'Создать сами кнопки (types.KeyboardButton(text="Текст, который будет написан на кнопке и который она будет отсылаться в чат"))'),
    InstructionContentElem('li', 'Добавить в объект из 1) кнопки из 2) с помощью метода add'),
    InstructionContentElem('li', 'В параметре reply_markup отсылаемого сообщения указать объект из 1). Тогда после того, как будет отослано это сообщение, кнопки появятся (Прим: при последующих перезапусках бота кнопки уже будут, они исчезнут только если удалить чат с ботом)'),
    InstructionContentElem('code', code10),
    InstructionContentElem('h2', ['Создание inline кнопок', 'inlinebutton_creating']),
    InstructionContentElem('p', 'Inline кнопки — кнопки под сообщением. Их функционал гораздо шире, чем у reply кнопок. Для создания inline кнопок надо:'),
    InstructionContentElem('li', 'Создать объект types.InlineKeyboardMarkup(row_width=количество кнопок в ряду под сообщением, по умолчанию 3)'),
    InstructionContentElem('li', 'Создать сами кнопки: types.InlineKeyboardButton(text="Текст кнопки", callback_data="любая строка")'),
    InstructionContentElem('li', 'Добавить в объект из 1) кнопки из 2) с помощью метода add'),
    InstructionContentElem('li', 'параметре reply_markup отсылаемого сообщения указать объект из 1). Тогда после того, как будет отослано это сообщение, кнопки появятся'),
    InstructionContentElem('li', 'Создать декоратор @bot.callback_query_handler(func=lambda call: True)'),
    InstructionContentElem('li', 'В нем написать функцию с 1 аргументом (назовем его call) и любым названием (назовем ее callback_inline)'),
    InstructionContentElem('li', 'Написать в ф-ии if call.message:'),
    InstructionContentElem('li', 'В ifе из 7) написать if call.data == "строка из callback_data пункта 2)":'),
    InstructionContentElem('li', 'прописать действие кнопки (например, отправку сообщения: bot.send_message(call.message.chat.id, "Пошел нахуй"))'),
    InstructionContentElem('code', code11),
    InstructionContentElem('p', 'Ну как бы все епта. Простенького бота теперь осилиш')
]
instruction = Instruction('telebot', content, chapter_list)
instruction.make_static(Path(static_pages, 'telebot.html'))
