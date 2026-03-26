import telebot
import database

from telebot import types

from sicret import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

users = database.load_data()

def click_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text='Нажми на меня!',
            callback_data='click'
        )
    )
    return keyboard

@bot.message_handler(commands=['start'])
def start_message(message):
    users[str(message.chat.id)] = 0
    bot.send_message(
        message.chat.id,
        text='Добро пожаловать!',
        reply_markup=click_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(callback):
    if callback.data == 'click':
        chat_id = callback.message.chat.id
        if str(chat_id) not in users:
            users[str(chat_id)] = 0

        users[str(chat_id)] += 1

        database.save_data(users)
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=callback.message.message_id,
            text=f'Счёт: {users[str(chat_id)]}',
            reply_markup=click_keyboard()
        )
    bot.answer_callback_quary(callback.id)

bot.infinity_polling()