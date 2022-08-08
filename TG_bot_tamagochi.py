

import random
import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text = 'Хочу пить', callback_data = '1')
    eat_btn = types.InlineKeyboardButton(text = 'Хочу есть', callback_data = '2')
    air_btn = types.InlineKeyboardButton(text='Хочу гулять', callback_data='3')
    slp_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    jk_btn = types.InlineKeyboardButton(text='Хочу шутку', callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(air_btn)
    keyboard.add(slp_btn)
    keyboard.add(jk_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, 'Добрый день! Выберите, что Вы хотите', reply_markup = keyboard)


@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('water.jpg', 'rb')
            bot.send_photo(chat_id = call.message.chat.id, photo = img, caption = 'Не дай себе засохнуть!)', reply_markup = keyboard )
            img.close()
        if call.data == '2':
            img = open('eat.jpg', 'rb')
            bot.send_photo(chat_id = call.message.chat.id, photo = img, caption = 'Приятного аппетита!)', reply_markup = keyboard )
            img.close()
        if call.data == '3':
            img = open('air.jpeg', 'rb')
            bot.send_photo(chat_id = call.message.chat.id, photo = img, caption = 'Юххууууу!!!)))', reply_markup = keyboard )
            img.close()
        if call.data == '4':
            img = open('slp.jpg', 'rb')
            bot.send_photo(chat_id = call.message.chat.id, photo = img, caption = 'Сладких снов...', reply_markup = keyboard )
            img.close()
        if call.data == '5':
            a = random.randint(1, 5)
            if a == 1:
                img = open('j1.jpg', 'rb')
                bot.send_photo(chat_id = call.message.chat.id, photo = img, reply_markup = keyboard )
                img.close()
            elif a == 2:
                img = open('j2.jpg', 'rb')
                bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=keyboard)
                img.close()
            elif a == 3:
                img = open('j3.JPG', 'rb')
                bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=keyboard)
                img.close()
            elif a == 4:
                img = open('j4.jpg', 'rb')
                bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=keyboard)
                img.close()
            else:
                img = open('j5.jpg', 'rb')
                bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=keyboard)
                img.close()
if __name__ == '__main__':
    bot.polling(none_stop = True)

