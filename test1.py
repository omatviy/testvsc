# -*- coding: utf-8 -*-
from gtts import gTTS
import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say "+words)


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        action = r.recognize_google(audio, language="ru-RU").lower()
        talk(action)
    except sr.UnknownValueError:
        talk("Я вас не поняла")


talk("Привет. Меня зовут Сири")
command()
url = "https://itproger.com"
webbrowser.open(url)
print("єто все")
# talk("як тебе звати?")
# talk("Будемо множити два числа")
#a=int(input("Введіть число 1:"))
#b=int(input("Введіть число 2:"))

# if (a>b):
#    print("a")
# else:
#    print("b")

# mas = [1,2,3,4,5]
# s = 0
# for i in mas:
#     s+=i

# print(s)
# a = int(input("a = "))
# b = int(input("b = "))
# c = a*b
# str_c = str(a) + "*" + str(b) + "=" + str(c)
# talk(str_c)
