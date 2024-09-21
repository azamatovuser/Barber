from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)


add_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить товар 🦍"), KeyboardButton(text="Посмотреть все товары")]
], resize_keyboard=True)
