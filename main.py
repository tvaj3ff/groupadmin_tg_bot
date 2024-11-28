import asyncio
import contextlib
from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging
from dotenv import load_dotenv, find_dotenv
import os

# Try to load environment variables from .env file
dotenv_path = find_dotenv()
if not dotenv_path:
    logging.warning(".env file not found")
else:
    load_dotenv(dotenv_path)

# Fetch the sensitive information from environment variables with default values
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ADMIN_ID = int(os.getenv("ADMIN_ID"))


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = ("Olá beleza 👋🏻👸🏻 Estou aqui para te mostrar uma maneira legal de ganhar comigo.\n"
           "\nSou o bot da Samira e posso te enviar as melhores ofertas se você me escrever agora mesmo 🤖\n"
           "\nMe escreve 👉🏻@Samira_Rod_vip")
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as exc:
        logging.error(f'[Exception] - {exc}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
