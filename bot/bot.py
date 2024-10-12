import os
import asyncio
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

load_dotenv()


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
# Диспетчер
dp = Dispatcher()


@dp.message(Command("game"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Орел", url="http://localhost:8080/user_choice?choice=Орел")
    )
    builder.row(types.InlineKeyboardButton(
        text="Решка",
        url="http://localhost:8080/user_choice?choice=Решка")
    )

    await message.answer(
        'Сделайте выбор',
        reply_markup=builder.as_markup(),
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())