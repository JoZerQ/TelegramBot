import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6475496025:AAE4y0J6CgXyN3_Mot9FnKgM48jU3-DJycE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)