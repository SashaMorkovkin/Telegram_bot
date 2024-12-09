from aiogram import types, F, Router
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message
from keyboards import inline_cars, settings

router = Router()


@router.message(Command('help'))
async def start_cmd(message: types.Message):
    await message.answer(f"Приветствую, это была комманда: {message.text}")


@router.message(CommandStart())
async def get_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}\nТвой ID: {message.from_user.id}\n',
                        reply_markup=await settings())


@router.message(Command('cars'))
async def get_cars(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}\nТвой ID: {message.from_user.id}\n',
                        reply_markup=await inline_cars())