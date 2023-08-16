from aiogram import Bot, Dispatcher, executor, types
from decouple import config

bot = (config("API_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.message):
    await message.reply("Hello, I'm the bot-shop assistant!\nCan I help you with something?")
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


