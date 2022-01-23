from google.auth.crypt import rsa
import config
import telebot
import translatingstuff
import firebase
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    get_list_button = types.KeyboardButton('Мой словарик 📖')
    markup.add(get_list_button)
    bot.send_message(message.chat.id, 'Привет! \n Я бот переводчик, напиши мне слово и я переведу его с русского на английский или наоборот.',
    reply_markup=markup)

@bot.message_handler(commands=['mylist'])
def getter(message):
    users_storage = firebase.get_users_data(message.chat.id)
    bot.send_message(message.chat.id, users_storage)

# добавить подтверждение запроса
@bot.message_handler(commands=['delete'])
def delete(message):
    firebase.delete_the_user(message.chat.id)
    bot.send_message(message.chat.id, 'Профиль успешно удален')


@bot.message_handler(content_types=['text'])
def replyer(message):
    if message.chat.type == 'private':
        if message.text == 'Мой словарик 📖':
            getter(message)
        else:
            result = translatingstuff.translatethis(message.text)
            bot.send_message(message.chat.id, result)
            firebase.add_data(message.chat.id, message.text, result)




    
# RUN
bot.polling(none_stop=True)

