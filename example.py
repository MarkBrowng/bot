from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# регистрация обработчика для всех сообщений, используя декоратор
@dp.message_handler()
async def echo_message(msg: types.Message): # ассинхронная функция для пересылки полученного сообщения
   # msg - это объект сообщения, который содержит данные о полученном сообщении и его отправители
   await bot.forward_message(msg.from_user.id, msg.from_user.id, msg.message_id)
   # msg.from_user.id - уникальный идентификатор пользователя, отправившего сообщение

if __name__ == '__main__':
   executor.start_polling(dp)