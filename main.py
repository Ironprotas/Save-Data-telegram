import shutil
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from Setting import config

logging.basicConfig(level=logging.INFO)
bot =  Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

@dp.message()
async def cmd_download(message: types.Message, bot : Bot ):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    name_file = f"{message.document.file_name}"
    await bot.download_file(file_path, name_file)
    shutil.move(name_file, "Data")
    await message.answer("I saved file")

@dp.message()
async  def cmd_download_link(message: types.Message, bot :Bot):
    pass

async def main():
    await dp.start_polling(bot)
    dp.message.register(cmd_download, Command("Download"))

if __name__ == "__main__":
    asyncio.run(main())