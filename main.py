from aiogram import Bot, Dispatcher, executor, types
from app import keyboard as kb
from app import database as db
from dotenv import load_dotenv
import openai
import os
import logging

logging.basicConfig(level=logging.DEBUG)


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

openai.api_key = os.getenv('CHAT_GPT')

async def on_startup(_):
    await db.db_start()
    print("Бот успешно запущен")



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await db.cmd_start_db(message.from_user.id)
    await message.answer_sticker('CAACAgEAAxkBAAMzZC3SnsEo6kiydveWR0vsy31b1GEAAgYAA1qqCUyCbvObrMeIKi8E')
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли как администратор!', reply_markup=kb.main_admin)
    elif message.from_user.id == int(os.getenv('CLASS_BAKTIAR_ID')):
        await message.answer(f'👋 Добро пожаловать!Вы успешно зашли как ученик!', reply_markup=kb.main_class)
    elif message.from_user.id == int(os.getenv('TEST_MAMA_ID')):
        await message.answer(f'👋 Добро пожаловать!Вы успешно зашли как ученик!', reply_markup=kb.main_class)
    else:
        await message.answer(f'{message.from_user.first_name},👋 Добро пожаловать! Чтобы начать пользоваться ботом нажмите на кнопку "Верификация"', reply_markup=kb.unverified_one)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(message.sticker.file_id)



@dp.message_handler(text='📄Гдз')
async def gdz(message: types.Message):
    await message.answer(f"❗Пока что доступен ГДЗ только 7 класса. Если у вас есть ГДЗ других классов то напишите создателю.", reply_markup=kb.gdzlist)



@dp.message_handler(text='🤖Нейросети')
async def bot(message: types.Message):
    await message.answer(f"🤖Вот список нейроситей которые помогут вам с уроками:'chatGPT-Нейросеть для написания эссе либо решение каких то заданий,"
                         f" DALL-E-Нарисует вам рисунок по вашему запросу."
                         f" ReText-перепишет ваш текст для антиплагията(Совместно с chatGPT)", reply_markup=kb.ai)


@dp.message_handler(text='Запустить ИИ')
async def startgpt(message: types.Message):
    await message.answer(f"Для запуска ИИ нажмите кнопку ниже. Для отключения перезапустите бота", reply_markup=kb.startGPT)


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'chatGPT':
        response = openai.Completion.create(
            model='text-davinci-003',
            promt=callback_query.data,
            temperature=1,
            max_tokens=2048,
            top_p=0.7,
        )
        await bot.send_message(response['choices'][0]['text'])





@dp.message_handler(text='🖋Обратная связь')
async def contacts(message: types.Message):
    await message.answer(f"🖋Вы можете написать создателю бота для того чтоб получить какие то сведения или просто подать идею для продвижения бота", reply_markup=kb.help)


@dp.message_handler(text='👥Чат')
async def chat(message: types.Message):
    await message.answer(f"👥Чат с учениками 69 гимазии: ", reply_markup=kb.ch)



@dp.message_handler(text='↩Назад')
async def back(message: types.Message):
    await message.answer(f'↩Вы вернулись назад', reply_markup=kb.main_class)

@dp.message_handler(text='Админ панель')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'log in', reply_markup=kb.adminpanel)
    else:
        await message.reply('error')

@dp.message_handler(text='Верификация')
async def verify(message: types.Message):
    await message.answer(f'Для верификации напишите в чат /id и отправьте код от бота создателю бота. Для того чтобы написать создателю нажмите на кнопку "Написать создателю"', reply_markup=kb.unverifiedtwo)

@dp.message_handler(text='Написать создателю')
async def verify_two(message: types.Message):
    await message.answer(f'Напишите ему для верификации: @soquoru')



@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Ваш запрос пока что не понятен боту.")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
