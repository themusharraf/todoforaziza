from aiogram import types, Router
from aiogram.filters import Command

from service import add_task, list_tasks, edit_task, delete_task

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("TODO botga xush kelibsiz! Quyidagi buyruqlar mavjud:\n"
                        "/add <vazifa> - Vazifa qo‘shish\n"
                        "/list - Vazifalarni ko‘rish\n"
                        "/edit <id> <yangi matn> - Vazifani o‘zgartirish\n"
                        "/delete <id> - Vazifani o‘chirish")


@router.message(Command("add"))
async def add_task_command(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply("Vazifa matnini kiriting: /add <vazifa>")
        return
    task = parts[1]
    add_task(message.from_user.id, task)
    await message.reply("✅ Vazifa qo‘shildi!")


@router.message(Command("list"))
async def list_tasks_command(message: types.Message):
    tasks = list_tasks(message.from_user.id)
    if not tasks:
        await message.reply("Sizda hozircha vazifalar yo‘q.")
    else:
        tasks_text = "\n".join([f"{task['id']}. {task['description']} - {task['status']}" for task in tasks])
        await message.reply(f"📋 Sizning vazifalaringiz:\n{tasks_text}")


@router.message(Command("edit"))
async def edit_task_command(message: types.Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.reply("To‘liq ma’lumot kiriting: /edit <id> <yangi matn>")
        return
    task_id, new_text = parts[1], parts[2]
    if edit_task(message.from_user.id, task_id, new_text):
        await message.reply("🔄 Vazifa yangilandi!")
    else:
        await message.reply("❌ Vazifa topilmadi!")


@router.message(Command("delete"))
async def delete_task_command(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply("Vazifa IDni kiriting: /delete <id>")
        return
    task_id = parts[1]
    if delete_task(message.from_user.id, task_id):
        await message.reply("🗑 Vazifa o‘chirildi!")
    else:
        await message.reply("❌ Vazifa topilmadi!")
