import telebot
import schedule
from threading import Thread
from dict import data


bot = telebot.TeleBot('5449907668:AAGk3bPYK0RatF-A7LHzpmfHPhARin3ZERE')
photo = 'https://media.discordapp.net/attachments/1020346164505219092/1063730044075261983/IMG_20230114_110257_603.jpg'
chat_id = 0


@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    text1 = 'Привет! Это бот по уходу за цветами школы 1561.'
    text2 = 'Я буду присылать напоминания о необходимости полить цветы. Также ты можешь напсиать '
    text3 = '/(номер на горшке), чтобы узнать информацию о растении.'
    text = text1+'\n'+text2+'\n'+text3
    bot.send_photo(chat_id, photo, caption=text)


@bot.message_handler()
def number(message):
    global chat_id
    chat_id = message.chat.id
    if message.text == '/1' or message.text == '/1@sch1561_plants_bot':
        photo1 = data['1']['pict']
        bot.send_photo(chat_id, photo1, caption=data['1']['name']+'\n'+data['1']['desc'])
    elif message.text == '/2' or message.text == '/2@sch1561_plants_bot':
        photo2 = data['2']['pict']
        bot.send_photo(chat_id, photo2, caption=data['2']['name']+'\n'+data['2']['desc'])
    elif message.text == '/3' or message.text == '/3@sch1561_plants_bot':
        photo3 = data['3']['pict']
        bot.send_photo(chat_id, photo3, caption=data['3']['name']+'\n'+data['3']['desc'])
    elif message.text == '/4' or message.text == '/4@sch1561_plants_bot':
        photo4 = data['4']['pict']
        bot.send_photo(chat_id, photo4, caption=data['4']['name']+'\n'+data['4']['desc'])
    elif message.text == '/5' or message.text == '/5@sch1561_plants_bot':
        photo5 = data['5']['pict']
        bot.send_photo(chat_id, photo5, caption=data['5']['name']+'\n'+data['5']['desc'])
    elif message.text == '/6' or message.text == '/6@sch1561_plants_bot':
        photo6 = data['6']['pict']
        bot.send_photo(chat_id, photo6, caption=data['6']['name']+'\n'+data['6']['desc'])


def reminder1():
    bot.send_photo(chat_id, photo, caption='Нужно полить цветы /1, /2 и /3!')


def reminder2():
    bot.send_photo(chat_id, photo, caption='Нужно полить цветы /4, /5 и /6!')


def main():
    schedule.every().monday.at('10:15').do(reminder1)
    schedule.every().tuesday.at('10:15').do(reminder2)
    schedule.every().thursday.at('10:15').do(reminder1)
    schedule.every().friday.at('10:15').do(reminder2)
    schedule.every(90).seconds.do(reminder1)
    schedule.every(90).seconds.do(reminder2)

    while True:
        schedule.run_pending()


thread = Thread(target=main)
thread.start()
bot.polling(none_stop=True)
