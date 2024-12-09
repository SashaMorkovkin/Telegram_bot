from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Корзина')]
], resize_keyboard=True, input_fuild_placeholder='Выберите пункт меню.')

settings = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Telegram", url='https://web.telegram.org/a/#1115635044')]])


cars = ['Tesla', 'BMW', "Wolswagen"]


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/watch?v=vW-BMMXwk6o'))
    return keyboard.adjust(2).as_markup()