from aiogram import Bot, Dispatcher, executor, types
from decouple import config

bot = (config("API_TOKEN"))
dp = Dispatcher(bot)
# bot = Bot("6475496025:AAE4y0J6CgXyN3_Mot9FnKgM48jU3-DJycE")
# dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.message):
    await message.reply("Hello, I'm the bot-shop assistant!\nCan I help you with something?")
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


# import os
# import random
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from decouple import config

# bot = Bot(config("API_TOKEN"))
# dp = Dispatcher(bot)


# image_categories = {
#     'природа': 'nature',
#     'люди': 'people',
#     'космос': 'space'
# }

# image_paths = {
#     'nature': ['path_to_nature_image1', 'path_to_nature_image2', ...],
#     'people': ['path_to_people_image1', 'path_to_people_image2', ...],
#     'space': ['path_to_space_image1', 'path_to_space_image2', ...]
# }

# @dp.message_handler()
# async def handle_message(message: types.Message):
#     for keyword, category in image_categories.items():
#         if keyword in message.text.lower():
#             random_image = random.choice(image_paths[category])
#             with open(random_image, 'rb') as photo:
#                 await message.reply_photo(photo, caption=f'Random image from {category}')
#             return

#     await message.reply("Не розумію, що ви хочете. Спробуйте щось інше.")

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
