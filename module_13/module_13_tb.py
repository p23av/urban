from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7525918010:AAFEEkodAhNgI4WABgEOqrvWtElU2Dz4Zfs'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['Urban', 'aa'])
async def urban_message(message):
    print('urban msg')

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Start msg')

@dp.message_handler()
async def all_message(message):
    print('мы получили сообщение!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)