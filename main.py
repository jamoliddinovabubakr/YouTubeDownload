# You Tube dow
import datetime
import telebot
from telebot import types
from pytube import YouTube
from pytube import Playlist

link = ""

bot = telebot.TeleBot('5401702475:AAHKBwN-MjZ13RTnXmy3uhz_SQC3Nt2pz8g')
name = ''
group = ''
time_input = 0
time_output = 0
loc = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Отправьте ссылу: ")
    p = Playlist('https://www.youtube.com/playlist?list=PLRs8EELOYKc7DYIQixlV1s4EH5SR3TdNB')
    j = 1
    for i in p:
        print(f"{j}: {i}")
        yt = YouTube(i)
        stream = yt.streams.get_highest_resolution()
        stream.download()
bot.polling()




