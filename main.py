import asyncio
import logging
import sys
from os import getenv

import wikipedia
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv("6967414595:AAHaVXIEMl6ngSsAohhpVYIXTq1uhPKswkE")

dp = Dispatcher()

wikipedia.set_lang('uz')
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, Wikipedia Botiga xush kelibsiz! \n"
                         f"Botdan foydalanish uchun qidirmoqchi bo'lgan jumlanigzni kiriting! \n"
                         f"Masalan: 'O\'zbekiston'")


@dp.message()
async def wikipedia_handler(message: types.Message) -> None:
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("Bunday maqola mavjud emas!")


async def main() -> None:
    bot = Bot("6967414595:AAHaVXIEMl6ngSsAohhpVYIXTq1uhPKswkE", parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
