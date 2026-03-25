import telebot
from telebot import types

def start_keyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		types.KeyboardButton(text='😀 Привет')
	)

	return keyboard

def hru_keyboard():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(
			text = 'Хорошо',
			callback_data = 'good'
        ),
		types.InlineKeyboardButton(
			text = 'Плохо',
			callback_data='bad'
        )
    )
	return keyboard