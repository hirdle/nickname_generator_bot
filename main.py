import telebot
from telebot import types
from config import API_KEY_BOT, languages
from nickname_generator import generate as nick_generate

bot = telebot.TeleBot(API_KEY_BOT, parse_mode=None)

def create_base_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("New nickname")
    markup.add(item1)

    return markup

def back_start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("New nickname")
    markup.add(item1)

    bot.send_message(message.chat.id, "Сhoose command:", reply_markup=create_base_keyboard())

@bot.message_handler(commands=['start'])
def start(message):
    back_start_menu(message)

@bot.message_handler(content_types=['text'])
def send_photo(message):
    if message.text.strip() == 'New nickname':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for i in languages:
            item = types.KeyboardButton(i)
            markup.add(item)
        back_item = types.KeyboardButton("Back to menu")
        markup.add(back_item)
        
        bot.send_message(message.chat.id, "Choose language: ", reply_markup=markup)

        bot.register_next_step_handler(message, generate_nick)
        
    elif message.text.strip() == 'Back to menu':
        back_start_menu(message)

    else:
        bot.send_message(message.chat.id, nick_generate(languages[message.text]))

def generate_nick(message):
    bot.send_message(message.chat.id, nick_generate(languages[message.text]))

bot.polling(none_stop=True)