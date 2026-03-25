import telebot
import keyboards
from telebot import types

from sicret import API_TOKEN
from lists import greetings

bot = telebot.TeleBot(API_TOKEN)
	
@bot.message_handler(commands=['hello']) #отреагировать на команду
def send_welcome(message):
	bot.send_message(
		message.chat.id, 
		'Привет, я бот!'
	)

@bot.message_handler(func = lambda message: message.text == 'Привет') #отреагировать на сообщение
def say_hello(message):
	bot.send_message(
		message.chat.id, 
  		'Привет, как там?'
	)

@bot.message_handler(func = lambda message: message.text.lower() == 'привет') #отреагировать на сообщение с неважно каким регистром
def small_registooor(message):
	bot.send_message(
		message.chat.id, 
		'Привет, как там?'
	)

@bot.message_handler(func = lambda message: 'привет' in message.text.lower() ) #отреагировать на сообщение в котором есть "привет" насрать какой регистр
def kak_tam(message):
	bot.send_message(
		message.chat.id, 
  		'Привет, как там?'
	)

@bot.message_handler(func = lambda message: any(greeting in message.text.lower() for greeting in greetings)) #отреагировать на слова в списке greetings 
def privetic(message):
	bot.send_message(
		message.chat.id, 
  		text='Привет, как там?',
		reply_markup=keyboards.hru_keyboard
	)

@bot.message_handler(commands=['start'])
def started(message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		types.KeyboardButton(text='😀 Привет')
	)

	bot.send_message(
		message.chat.id, 
		text = 'Как дела?', 
		reply_markup=keyboards.hru_keyboard()
	)

@bot.message_handler()
def echo_all(message):
	bot.send_message(
		message.chat.id,
		'Ты вообще?'
	)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(callback):
	bot.answer_callback_query(callback.id)

	if callback.data == 'good':
		bot.send_message(
			callback.message.chat.id,
			text='Круто'
		)
	elif callback.data == 'bad':
		bot.send_message(
			callback.message.chat.id,
			text='Поплач'
		)

bot.infinity_polling()