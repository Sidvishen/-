from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ('7104415538:AAFJFVuLi5eALVknElHS_KEnp6nq1C9VMWU')
bot = Bot(token= api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text =['Хэй!'])
async def start(message):
    await message.answer ('Нажмите на команду /start, чтобы начать общение.')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer ('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    print("не назначеные сообщения")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
