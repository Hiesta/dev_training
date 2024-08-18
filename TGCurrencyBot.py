import datetime
import telebot
import redis
import time


course_url = 'https://apps.skillfactory.ru/learning/course/course-v1:Skillfactory+PDEVPRO+2023/home'
TOKEN = '7006631554:AAH3IK9ve4i0mErwMz6sU0Eh4ExBLXQszQo'
auth = False
redi = redis.Redis(
    host='redis-18121.c328.europe-west3-1.gce.redns.redis-cloud.com',
    port='18121',
    password='IvJs2Ogfa7bFkLsDGknAyPvmKx4hX0De'
)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def greet_reply(message):
    if message.chat.username == 'Shchepankovskaya':
        global auth
        auth = True
    if message.text == '/start':
        print(message.chat.username)
        bot.send_message(message.chat.id, f'Welcome, {message.chat.username}\nWrite /help to get available commands')
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'Helping...')


@bot.message_handler(content_types=['text',])
def checker(message):
    if message.text == 'password: merlin5583':
        bot.send_message(message.chat.id, 'Authorization completed')
        global auth
        auth = True
    elif any([message.text == 'admin',
              message.text == 'birthdays',
              message.text == 'anime',
              message.text == 'tv series',
              message.text == 'course']) and not auth:
        bot.send_message(message.chat.id, 'Enter admin password:')
    elif message.text == 'course' and auth:
        bot.send_message(message.chat.id, course_url)
    elif message.text == 'admin' and auth:
        bot.send_message(message.chat.id, f'Token = {TOKEN}')
    elif message.text == 'anime':
        bot.send_message(message.chat.id, f'1: Get anime list\n2: Add anime\n3: Delete anime')






def anime_add(message, user):
    bot.send_message(message.chat.id, 'Enter anime name:')
    redi.set(user, )


@bot.message_handler(content_types=['photo',])
def photo_reply(message):
    bot.reply_to(message, 'Nice meme XDDD')


bot.polling(non_stop=True)

