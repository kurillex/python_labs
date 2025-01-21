import json
import requests
import speech_recognition as sr
from currencies import print_currencies


def get_api():
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    response_analysis(response)
    return response


def response_analysis(response):
    if response.status_code != 200:
        print(response)


def get_info_from_response(response):
    data = json.loads(response.text)
    return data


def recognize_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Назовите валюту из списка: ")
        print_currencies()

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source, timeout=3)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вывод валюты: " + text + '\n')
            return text
        except sr.UnknownValueError:
            print("Речь не распознана.")
            return 'Fail'