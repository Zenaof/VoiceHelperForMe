# import pathlib
# import vosk
# import pyaudio
# from configVH import porcupine
# from pathlib import Path
# import json
#
# modelVoskLarge = False
# if modelVoskLarge:
#     modelVosk = 'vosk-model-large'
# else:
#     modelVosk = 'vosk-model-small'
#
# dir_path = pathlib.Path.cwd()
# path = pathlib.Path(dir_path, 'new-model', 'vosk-models', f'{modelVosk}')
#
# samplerate = 16000
# device = 1
#
# def load_model():
#     global model, kaldi_rec
#     try:
#         model = vosk.Model(str(path))
#         kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
#     except Exception as e:
#         print("Произошла ошибка при загрузке модели:", e)
#
# def Recognition():
#     try:
#         p = pyaudio.PyAudio()
#         stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True,
#                         frames_per_buffer=porcupine.frame_length)
#
#         while True:
#             data = stream.read(porcupine.frame_length)
#             if kaldi_rec.AcceptWaveform(data):
#                 result = json.loads(kaldi_rec.Result())
#                 user_speech = result.get('text', '')
#                 return user_speech
#     except Exception as e:
#         print("Произошла ошибка при распознавании речи:", e)
#     finally:
#         stream.stop_stream()
#         stream.close()
#         p.terminate()

import pathlib
import vosk
import json
import pyaudio
from configVH import porcupine
from pathlib import Path

# Выбор можели воск маленькая или большая
modelVoskLarge = False
if modelVoskLarge == True:
    modelVosk = 'vosk-model-large'
else:
    modelVosk = 'vosk-model-small'

# Настройка путей к файлам и других параметров
dir_path = pathlib.Path.cwd()
path = pathlib.Path(dir_path, 'new-model', 'vosk-models', f'{modelVosk}')

samplerate = 16000
device = 1

# Функция для распознавания речи

try:
    # Инициализация модели
    model = vosk.Model(str(path))
    kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
except Exception as e:
    # Обработка ошибок при инициализации модели
    print("Произошла ошибка:", e)

def load_model():
    global model, kaldi_rec
    try:
        model = vosk.Model(str(path))
        kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
    except Exception as e:
        print("Произошла ошибка при загрузке модели:", e)

def Recognition():
    try:
        # Инициализация PyAudio
        p = pyaudio.PyAudio()

        # Открытие аудиопотока
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True,
                        frames_per_buffer=porcupine.frame_length)

        while True:
            # Чтение данных из аудиопотока
            data = stream.read(porcupine.frame_length)

            # Попытка распознавания речи
            if kaldi_rec.AcceptWaveform(data):
                result = json.loads(kaldi_rec.Result())
                user_speech = result.get('text', '')
                return user_speech

    except Exception as e:
        # Обработка ошибок
        print("Произошла ошибка при распознавании речи:", e)

    finally:
        # Закрытие аудиопотока и освобождение ресурсов PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()


# Основной код для проверки
# if __name__ == "__main__":
#     while True:
#         # Инициализация рекогнайзера
#         try:
#             # Вызов функции распознавания речи
#             recognized_text = Recognition()
#             print("Распознанный текст:", recognized_text)
#
#         except Exception as e:
#             # Обработка ошибок при рекогнайзе
#             print("Произошла ошибка:", e)






#
#
# dir_path = pathlib.Path.cwd()
# path = Path(dir_path, 'new-model', 'vosk-models', f'{modelVosk}')
#
# model = vosk.Model(fr'{path}') # полный путь к модели
# samplerate = 16000
# device = 1
# porcupine = config.porcupine
# kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
# def Recognition():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=config.porcupine.frame_length)
#
#     while True:
#         data = stream.read(porcupine.frame_length)
#         if kaldi_rec.AcceptWaveform(data):
#             result = json.loads(kaldi_rec.Result())
#             user_speech = result.get('text', '')
#             return user_speech
