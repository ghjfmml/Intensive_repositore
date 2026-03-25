import telebot
from telebot import types

from sicret import API_TOKEN
from lists import greetings

bot = telebot.TeleBot(API_TOKEN)

def start_keyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		types.KeyboardButton(text='😀 Привет')
	)

	return keyboard
	
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

@bot.message_handler(func = lambda message: message.text.lower() == 'привет') #отреагировать на маленький регистр
def small_registooor(message):
	bot.send_message(
		message.chat.id, 
		'Привет, как там?'
	)

@bot.message_handler(func = lambda message: 'привет' in message.text.lower() ) #отреагировать на сообщение насрать какой регистр
def kak_tam(message):
	bot.send_message(
		message.chat.id, 
  		'Привет, как там?'
	)

@bot.message_handler(func = lambda message: any(greeting in message.text.lower() for greeting in greetings))
def privetic(message):
	bot.send_message(
		message.chat.id, 
  		'Привет, как там?'
	)

@bot.message_handler(commands=['start'])
def started(message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		types.KeyboardButton(text='😀 Привет')
	)

	bot.send_message(message.chat.id, text = 'Бот запущен', reply_markup=keyboard)

@bot.message_handler()
def echo_all(message):
	bot.send_message(
		message.chat.id,
		'Ты вообще?'
	)

bot.infinity_polling()