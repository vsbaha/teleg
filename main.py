from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from app import keyboard as kb
from app import database as db
from dotenv import load_dotenv
# import openai
import os
import logging

# Это логи
logging.basicConfig(level=logging.DEBUG)
storage = MemoryStorage()

# Это настройка аиграм
storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv('TOKEN_MAIN'))
dp = Dispatcher(bot, storage=storage)


# это люди в вайтлисте
WHITE_LIST = [1189473577, 5038943885, 1992223776]

# это сообщение при страрте бота
async def on_startup(_):
    await db.db_start()
    print("Бот успешно запущен")


class MsgToAnon(StatesGroup):
    type = State()
    text = State()
    name = State()

# это старт бота и проверка айди
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await db.cmd_start_db(message.from_user.id)
    await message.answer_sticker('CAACAgEAAxkBAAMzZC3SnsEo6kiydveWR0vsy31b1GEAAgYAA1qqCUyCbvObrMeIKi8E')
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'👋👋Вы вошли как администратор!', reply_markup=kb.main_admin)
    elif message.from_user.id in WHITE_LIST:
        await message.answer(f'👋👋 Добро пожаловать!Вы успешно зашли как ученик!', reply_markup=kb.main_class)
    else:
        await message.answer(f'{message.from_user.first_name},👋 Добро пожаловать! Чтобы начать пользоваться ботом нажмите на кнопку "Верификация"', reply_markup=kb.unverified_one)

# это для получения айди юзера
@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

# это для айди стикера
@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(message.sticker.file_id)

# это гдз всех классов
@dp.message_handler(text='4-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Пока что пусто!", reply_markup=kb.gdzlist_4_class)

@dp.message_handler(text='5-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Пока что пусто!", reply_markup=kb.gdzlist_5_class)

@dp.message_handler(text='6-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Пока что пусто!", reply_markup=kb.gdzlist_6_class)

@dp.message_handler(text='7-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Вот все доступные гдз для 7 класса", reply_markup=kb.gdzlist_7_class)

@dp.message_handler(text='8-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Пока что пусто!", reply_markup=kb.gdzlist_8_class)

@dp.message_handler(text='9-класс')
async def gdz_4_class(message: types.Message):
    await message.answer(f"Пока что пусто!", reply_markup=kb.gdzlist_9_class)

# это хендлер для гдз
@dp.message_handler(text='📄Гдз')
async def gdz_lessons(message: types.Message):
    await message.answer(f"❗Пока что доступен ГДЗ только 7 класса. Если у вас есть ГДЗ других классов то напишите создателю.", reply_markup=kb.gdz_class)


# это для ии
@dp.message_handler(text='🤖Нейросети')
async def bot(message: types.Message):
    await message.answer(f"Вот список нейроcетей которые помогут вам с урокаи:\nChatGPT-Напишет эссе \nDALL-E-Нарисует картинку по вашему запросу \nReText-Переделает ваш текст для уникальности", reply_markup=kb.ai)


# это бекап
@dp.message_handler(text='🖋Обратная связь')
async def contacts(message: types.Message):
    await message.answer(f"🖋Вы можете написать создателю бота для того чтоб получить какие то сведения или просто подать идею для продвижения бота", reply_markup=kb.help)


# это чат
@dp.message_handler(text='👥Чат')
async def chat(message: types.Message):
    await message.answer(f"👥Чат с учениками 69 гимазии: ", reply_markup=kb.ch)


# это назад
@dp.message_handler(text='↩Назад')
async def back(message: types.Message):
    await message.answer(f'↩Вы вернулись назад', reply_markup=kb.main_class)


# это админ панель
@dp.message_handler(text='Админ панель')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'log in', reply_markup=kb.adminpanel)
    else:
        await message.reply('error')

@dp.message_handler(text='Отправить сообщение в анонимку')
async def send_anon(message: types.Message):
    await MsgToAnon.type.set()
    await message.answer(f'что вы хотите сделать', reply_markup=kb.ch)

@dp.callback_query_handler(state=MsgToAnon.type)
async def send_anon_type(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = call.data
    await call.message.answer(f'Напишите ваше анонимное сообщение', reply_markup=kb.cancel)
    await MsgToAnon.next()

@dp.callback_query_handler(state=MsgToAnon.text)
async def send_anon_text(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = call.data
    await call.message.answer(f'Напишите ваше имя. если хотите не писать то просто напишите нижнее подчеркивание(_)', reply_markup=kb.cancel)
    await MsgToAnon.next()

@dp.callback_query_handler(state=MsgToAnon.name)
async def send_anon_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = call.data
    await db.send_anon(state)
    await call.message.answer(f'Done!', reply_markup=kb.main_class)
    await state.finish()

# это система верификации(надо изменить)
@dp.message_handler(text='Верификация')
async def verify(message: types.Message):
    await message.answer(f'Для верификации напишите в чат /id и отправьте код от бота создателю бота. Для того чтобы написать создателю нажмите на кнопку "Написать создателю"', reply_markup=kb.unverifiedtwo)

@dp.message_handler(text='Написать создателю')
async def verify_two(message: types.Message):
    await message.answer(f'Напишите ему для верификации: @soquoru')


# это ответ на неопнятный запрос
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Ваш запрос пока что не понятен боту.")

# это для корректной работы бота
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)



# response = openai.Completion.create(
#             model='text-davinci-003',
#             promt=message.text,
#             temperature=1,
#             max_tokens=2048,
#             top_p=0.7,
#             frequency_penalty=0
#               )
#               await bot.send_message(response['choices'][0]['text'])
