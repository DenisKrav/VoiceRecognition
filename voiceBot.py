# При додані блоку з погодою, врахувати, що треба казати американські міста

import speech_recognition as sr
import subprocess
import webbrowser
import pyowm
import translators as ts
import gpt
import gtts
import os

recognizer = sr.Recognizer()

owm = pyowm.OWM('5817d6a145c443107efc34417e35c2ac')

def capture_voice_input():
    with sr.Microphone() as source:
        print("Слухаю...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language="uk-UK")
        print("Ви сказали: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Я не розумію вас")
    except sr.Recognizer as e:
        text = ""
        print("Помилка; {0}".format(e))
    return text

def process_voice_command(text):
    if "привіт" in text.lower():
        print("Привіт! Як я можу Вам допомогти?")
    elif "як справи" in text.lower():
        print("Супер, а у Вас?")
    elif "калькулятор" in text.lower():
        subprocess.call(['calc'])
    elif "логіка" in text.lower():
        webbrowser.open("https://learn.logikaschool.com/login")
    elif "youtube" in text.lower():
        webbrowser.open(f"https://youtube.com/results?search_query={text.lower()[7:]}")
    elif "погода" in text.lower():
        place = text[7:]
        place = ts.translate_text(place, from_language='uk', to_language='en')
        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather = "Температура (градусів Цельсію): " + str(int(weather.temperature('celsius')['temp']))
        print(weather)
    elif "джарвіс" in text.lower():
        result = gpt.generate(text + " and translate into Ukrainian. Don't print English words")
        print(result)
        try:
            myobj = gtts.gTTS(text=result, lang="uk", slow=False)
            myobj.save("result.mp3")
            os.system("result.mp3")
        except Exception as ex:
            print(ex)
            input()
    elif "код" in text.lower():
        code = gpt.generate(text + "і виведи тільки код")[3:-3]
        with open("generated_code.py", "w", encoding="utf-8") as file:
            file.write(code)
    elif "прощавай" in text.lower():
        print("До побачення! Гарного дня!")
        return True
    else:
        print("Я Вас не розумію. Повторіть Ваш запит")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()