import datetime
import json
import threading
import time
import num2words
from fuzzywuzzy import fuzz

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pathlib import Path
import stt
import tts
import voice_detection

class VoiceAssistantApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.models_loaded = False

    def load_models(self):
        print("Загрузка моделей начата...")
        try:
            stt.load_model()
            print("Модели успешно загружены.")
            self.models_loaded = True
            self.on_models_loaded()
        except Exception as e:
            print("Произошла ошибка при загрузке моделей:", e)

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.loading_label = Label(text='Загрузка моделей...', size_hint=(1, 0.2))
        self.layout.add_widget(self.loading_label)

        threading.Thread(target=self.load_models).start()

        return self.layout

    def on_models_loaded(self):
        print("Загрузка моделей завершена.")
        self.layout.clear_widgets()

        self.input = TextInput(hint_text='Скажите что-нибудь', size_hint=(1, 0.2), multiline=False)
        self.layout.add_widget(self.input)

        self.button = Button(text='Отправить', size_hint=(1, 0.2))
        self.button.bind(on_press=self.process_input)
        self.layout.add_widget(self.button)

        self.response_label = Label(text='Здесь будет ответ', size_hint=(1, 0.6))
        self.layout.add_widget(self.response_label)

        self.voice_button = Button(text='Голосовой ввод', size_hint=(1, 0.2))
        self.voice_button.bind(on_press=self.voice_input)
        self.layout.add_widget(self.voice_button)

        # Теперь, когда модели загружены, запускаем detect_keyword в отдельном потоке
        threading.Thread(target=self.detect_keyword_thread).start()

    def process_input(self, instance):
        if not self.models_loaded:
            self.response_label.text = "Подождите, идет загрузка моделей..."
            return

        user_speech = self.input.text
        command = self.command_filter(user_speech)
        if command:
            response = self.processing_commands(command)
            self.response_label.text = response
            tts.Checking_the_connection(response)
        else:
            self.response_label.text = "Команда не найдена или низкий коэффициент сходства."

    def voice_input(self, instance):
        if not self.models_loaded:
            self.response_label.text = "Подождите, идет загрузка моделей..."
            return

        self.response_label.text = "Слушаю..."
        user_speech = stt.Recognition()
        self.input.text = user_speech
        self.process_input(instance)

    def detect_keyword_thread(self):
        time.sleep(1)  # Добавим задержку для обхода конфликта при обновлении UI
        self.detect_keyword()

    def detect_keyword(self):
        if not self.models_loaded:
            print("Подождите, идет загрузка моделей...")
            if hasattr(self, 'response_label'):
                self.response_label.text = "Подождите, идет загрузка моделей..."
            return

        is_detected = voice_detection.callback(False)
        if is_detected:
            print("Обнаружено ключевое слово!")
            self.response_label.text = "Ключевое слово сработало!!!"
            self.voice_input(None)
        else:
            print("Ключевое слово не обнаружено.")

    def command_filter(self, user_speech):
        best_command = None
        max_ratio = 0

        for command in self.commands:
            activation_phrase = command['activation_phrase']
            ratio = fuzz.ratio(user_speech.lower(), activation_phrase.lower())
            if ratio > max_ratio:
                max_ratio = ratio
                best_command = command

        if best_command and max_ratio > 50:  # Пороговое значение сходства
            return best_command
        return None

    def processing_commands(self, command):
        if command['action'] == 'time':
            now = datetime.datetime.now()
            text = "Сейч+ас " + num2words.num2words(now.hour, lang='ru') + " " + num2words.num2words(now.minute, lang='ru')
            response_text = f"{command['response']} {text}"
        elif command['action'] == 'hello':
            response_text = f"{command['response']}"
        else:
            response_text = "Неизвестная команда"
        return response_text

if __name__ == '__main__':
    VoiceAssistantApp().run()