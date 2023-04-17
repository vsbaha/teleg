from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

unverified_one = ReplyKeyboardMarkup(resize_keyboard=True)
unverified_one.add('Верификация')

main_class = ReplyKeyboardMarkup(resize_keyboard=True)
main_class.add('📄Гдз').add('🤖Нейросети').add('👥Чат').add('Запустить ИИ').add('🖋Обратная связь')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('📄Гдз').add('🤖Нейросети').add('👥Чат').add('Запустить ИИ').add('🖋Обратная связь').add('Админ панель')

adminpanel = ReplyKeyboardMarkup(resize_keyboard=True)
adminpanel.add('Добавить гдз').add('Удалить гдз').add('Сделать рассылку').add('↩Назад')

unverifiedtwo = ReplyKeyboardMarkup(resize_keyboard=True)
unverifiedtwo.add('Верификация').add('Написать создателю')

gdzlist = InlineKeyboardMarkup(row_width=2)
gdzlist.add(InlineKeyboardButton(text='Алгебра', url='http://surl.li/foimj'),
            InlineKeyboardButton(text='Геометрия', url='http://surl.li/foiou'),
            InlineKeyboardButton(text='other', url='https://chat.openai.com/chat'))

ai = InlineKeyboardMarkup(row_width=2)
ai.add(InlineKeyboardButton(text='chatGPT', url='https://chat.openai.com/chat'),
       InlineKeyboardButton(text='DALL-E', url='https://labs.openai.com/'),
       InlineKeyboardButton(text='ReText', url='https://retext.ai/ru'))


help = InlineKeyboardMarkup(row_width=2)
help.add(InlineKeyboardButton(text='Написать создателю', url='https://t.me/soquoru'))

ch = InlineKeyboardMarkup(row_width=2)
ch.add(InlineKeyboardButton(text='Чат', url='https://t.me/+MqaYd4TYTfI2ZGM6'))

startGPT = InlineKeyboardMarkup(row_width=1)
startGPT.add(InlineKeyboardButton(text='Запустить ИИ', callback_data='chatGPT'))
