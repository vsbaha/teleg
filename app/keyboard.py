from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

unverified_one = ReplyKeyboardMarkup(resize_keyboard=True)
unverified_one.add('Верификация')

main_class = ReplyKeyboardMarkup(resize_keyboard=True)
main_class.add('📄Гдз').add('🤖Нейросети').add('👥Чат').add('🖋Обратная связь')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('📄Гдз').add('🤖Нейросети').add('👥Чат').add('🖋Обратная связь').add('Админ панель')

adminpanel = ReplyKeyboardMarkup(resize_keyboard=True)
adminpanel.add('Добавить гдз').add('Удалить гдз').add('Сделать рассылку').add('↩Назад')

unverifiedtwo = ReplyKeyboardMarkup(resize_keyboard=True)
unverifiedtwo.add('Верификация').add('Написать создателю')

gdz_class = ReplyKeyboardMarkup(resize_keyboard=True)
gdz_class.add('4-класс').add('5-класс').add('6-класс').add('7-класс').add('8-класс').add('9-класс').add('↩Назад')

gdzlist_4_class = InlineKeyboardMarkup(row_width=2)
gdzlist_4_class.add(InlineKeyboardButton(text='None', url='https://t.me/soquoru'),
                    InlineKeyboardButton(text='None', url='https://t.me/soquoru'))

gdzlist_5_class = InlineKeyboardMarkup(row_width=2)
gdzlist_5_class.add(InlineKeyboardButton(text='None', url='https://t.me/soquoru'),
                    InlineKeyboardButton(text='None', url='https://t.me/soquoru'))

gdzlist_6_class = InlineKeyboardMarkup(row_width=2)
gdzlist_6_class.add(InlineKeyboardButton(text='None', url='https://t.me/soquoru'),
                    InlineKeyboardButton(text='None', url='https://t.me/soquoru'))

gdzlist_7_class = InlineKeyboardMarkup(row_width=2)
gdzlist_7_class.add(InlineKeyboardButton(text='Алгебра', url='http://surl.li/foimj'),
                    InlineKeyboardButton(text='Геометрия', url='http://surl.li/foiou'))

gdzlist_8_class = InlineKeyboardMarkup(row_width=2)
gdzlist_8_class.add(InlineKeyboardButton(text='None', url='https://t.me/soquoru'),
                    InlineKeyboardButton(text='None', url='https://t.me/soquoru'))

gdzlist_9_class = InlineKeyboardMarkup(row_width=2)
gdzlist_9_class.add(InlineKeyboardButton(text='None', url='https://t.me/soquoru'),
                    InlineKeyboardButton(text='None', url='https://t.me/soquoru'))


ai = InlineKeyboardMarkup(row_width=2)
ai.add(InlineKeyboardButton(text='chatGPT', url='https://chat.openai.com/chat'),
       InlineKeyboardButton(text='DALL-E', url='https://labs.openai.com/'),
       InlineKeyboardButton(text='ReText', url='https://retext.ai/ru'))


help = InlineKeyboardMarkup(row_width=2)
help.add(InlineKeyboardButton(text='Написать создателю', url='https://t.me/soquoru'))

ch = InlineKeyboardMarkup(row_width=2)
ch.add(InlineKeyboardButton(text='Анонимка', url='https://t.me/+MqaYd4TYTfI2ZGM6'),
       InlineKeyboardButton(text='Отправить сообщение в анонимку', callback_data='send_message'))

# Создаем клавиатуру с одной кнопкой
inline_kb_full = InlineKeyboardMarkup(row_width=1)
inline_btn = InlineKeyboardButton('Нажми меня', callback_data='button_pressed')
inline_kb_full.add(inline_btn)

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('↩Назад')
