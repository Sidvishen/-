from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio

api = ('7104415538:AAFJFVuLi5eALVknElHS_KEnp6nq1C9VMWU')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
@dp.message_handler(text =['Привет'])
async def start(message):
    await message.answer('Нажмите на команду /start, чтобы начать общение.')
@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.'
                         'Вы можете ввести текст Calories для расчета коллорий.')
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(text =['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.answer(f"Теперь введите свой рост в сантиметрах.")
    await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=growth)
    await message.answer(f"Теперь введите свой вес в килограммах.")
    await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))
    calories = 88.362 + (13.397 * weight) + (4.799 * growth) - (5.677 * age)

    await message.answer(f'Ваш возраст - {age}                                                                                                                              '
                         f'Ваш рост - {growth} см                                                                                                                           '
                         f'Ваш вес - {weight} кг                                                                                                                            '
                         f'Ваша норма калорий = {calories:.2f}')
    await state.finish()

"""
Хендлер принимающие любые сообщения
"""
@dp.message_handler()
async def all_message(message):
    print("не назначеные сообщения")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
