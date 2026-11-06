from os import getenv
from pymongo import AsyncMongoClient
from vkbottle.bot import Bot
from dotenv import load_dotenv

if input() == "dev-mode":
    load_dotenv()
    print("Бот стартовал в dev режиме")

bot = Bot("GroupToken")


@bot.on.message()
async def handler(_) -> str:
    return "Hello, World!"


bot.run()
