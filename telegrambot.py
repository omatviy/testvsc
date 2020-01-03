import telebot
from gtts import gTTS
import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say "+words)


bot = telebot.TeleBot("929431619:AAFbRUH8KA3jBON1GRHiERENbA2qz0KJUbg")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    n = int(message.text)
    lst = list(range(1,n+1))

    sum = 0
    for i in lst:
        sum+=i

    
    talk(str(sum))
    bot.reply_to(message, str(sum))
    

bot.polling()
