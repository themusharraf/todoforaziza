from aiogram import Dispatcher
from handlers import todo


def register_all_handlers(dp: Dispatcher):
    dp.include_router(todo.router)
