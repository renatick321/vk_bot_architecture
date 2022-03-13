

from config import bot
from vkbottle.bot import Message




@bot.on.message(text="привет")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f"Hello, {users_info[0].first_name}")