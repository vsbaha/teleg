from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Гдз').add('Помощь').add('Помощь создателю')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Гдз').add('Помощь').add('Помощь создателю').add('Админ панель')

adminpanel = ReplyKeyboardMarkup(resize_keyboard=True)
adminpanel.add('Добавить гдз').add('Удалить гдз').add('Сделать рассылку')



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name},Добро пожаловать на бота ')
    await message.answer_sticker('CAACAgIAAxkBAAMaZBTgJnIRON_pM7EpHkJpmyubsB8AAgUAAwsieTNT4xP8FX5BVS8E',
                                 reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли как администратор!', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(text='Гдз')
async def gdz(message: types.Message):
    await message.answer(f"Напишите ему для поддержки: @soquoru")

@dp.message_handler(text='Помощь')
async def help(message: types.Message):
    await message.answer(f"Напишите ему для поддержки: @soquoru")

@dp.message_handler(text='Помощь создателю')
async def contacts(message: types.Message):
    await message.answer(f"Вы можете отправить ему сайты с гдз для каких то предметов или просто сообщить об ошибке или идею: @soquoru")

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
