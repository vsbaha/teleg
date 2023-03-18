from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Гдз').add('Нейросети').add('Чат').add('Помощь создателю')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Гдз').add('Нейросети').add('Чат').add('Помощь создателю').add('Админ панель')

adminpanel = ReplyKeyboardMarkup(resize_keyboard=True)
adminpanel.add('Добавить гдз').add('Удалить гдз').add('Сделать рассылку').add('Назад')


seven = ReplyKeyboardMarkup(resize_keyboard=True)
seven.add('Алгебра').add('Геометрия').add('Остальные предметы').add('Назад')

ai = ReplyKeyboardMarkup(resize_keyboard=True)
ai.add('chatGPT').add('DALL-E').add('ReText').add('Назад')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать! Этот бот создан для помощи учеников и просто для фана ')
    await message.answer_sticker('CAACAgIAAxkBAAMaZBTgJnIRON_pM7EpHkJpmyubsB8AAgUAAwsieTNT4xP8FX5BVS8E',
                                 reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли как администратор!', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(message.sticker.file_id)

@dp.message_handler(text='Гдз')
async def gdz(message: types.Message):
    await message.answer(f"Пока что доступны ГДЗ 7 класс. Если у вас есть ГДЗ других классов то напишите создателю.", reply_markup=seven)

@dp.message_handler(text='Алгебра')
async def alg(message: types.Message):
    await message.answer(f"Вот гдз по алгебре 7 класса: http://surl.li/foimj")


@dp.message_handler(text='Геометрия')
async def geom(message: types.Message):
    await message.answer(f"Вот гдз по алгебре 7 класса: http://surl.li/foiou")

@dp.message_handler(text='Остальные предметы')
async def other(message: types.Message):
    await message.answer(f'Для других предеметов используйте нейросети', reply_markup=ai)

@dp.message_handler(text='Нейросети')
async def bot(message: types.Message):
    await message.answer(f"Вот список нейроситей которые помогут вам с уроками:", reply_markup=ai)

@dp.message_handler(text='chatGPT')
async def gpt(message: types.Message):
    await message.answer(f'Эта нейросеть поможет вам ответить на ваш вопрос и может решить задачи по английскому: https://chat.openai.com/chat')

@dp.message_handler(text='DALL-E')
async def dalle(message: types.Message):
    await message.answer(f'Эта нейросеть сгенерирует вам картинку по вашему запросу: https://labs.openai.com/')

@dp.message_handler(text='ReText')
async def retext(message: types.Message):
    await message.answer(f'Эта нейросеть перепишет ваш текст так чтобы никто не догодался что вы его где то скопировали: https://retext.ai/ru')


@dp.message_handler(text='Помощь создателю')
async def contacts(message: types.Message):
    await message.answer(f"Вы можете отправить ему сайты с гдз для каких то предметов или просто сообщить об ошибке или идею: @soquoru")

@dp.message_handler(text='Чат')
async def chat(message: types.Message):
    await message.answer(f"Чат с учениками 69 гимазии: https://t.me/+MqaYd4TYTfI2ZGM6")

@dp.message_handler(text='Назад')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись назад', reply_markup=main)

@dp.message_handler(text='Админ панель')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'log in', reply_markup=adminpanel)
    else:
        await message.reply('error')





@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Ваш запрос пока что не понятен боту.")


if __name__ == '__main__':
        executor.start_polling(dp)
