import time
# import locDataBase
# import requests
# import voice_detection
import tts
# import stt
import os
from pathlib import Path

print(os.name)

path = Path('new-model', 'vosk-model-large')
print(str(path))

tts.Checking_the_connection('Приветик')

# def key_word_detect():
#     while True:
#         keyWord = voice_detection.callback(False)
#         if keyWord == True:
#             print('ключевое слово сработало!!!')
#
# key_word_detect()

# import json
# import pvporcupine
# import pyaudio
# import time
# from fuzzywuzzy import fuzz
# from vosk import Model, KaldiRecognizer
# import vosk
# import config
# from pvrecorder import PvRecorder

# with open('Json/commands.json', 'r') as file:
#     commands_data = json.load(file)
#     commands = commands_data.get('commands', [])
#
# porcupine = pvporcupine.create(access_key='1Z9KvyECJVK9skD58L9D0ayAhZI91t4fWDl7OFmI8VB9QXc1BRAIlQ==',
#                                keyword_paths=['Neyro/hey_gosha.ppn'])
#
# model = vosk.Model("vosk")
# samplerate = 16000
# device = config.MICROPHONE_INDEX
# kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
#
#
# def find_best_command(user_speech):
#     max_ratio = 0
#     best_command = None
#
#     for command in commands:
#         activation_phrase = command['activation_phrase']
#         ratio = fuzz.ratio(user_speech, activation_phrase)
#         if ratio > max_ratio:
#             max_ratio = ratio
#             best_command = command
#         if best_command and max_ratio > 10:
#             return best_command
#
#
# def execute_command(command):
#     if command['action'] == 'time':
#         current_time = time.strftime("%H:%M", time.localtime())
#         response_text = f"{command['response']} {current_time}"
#     elif command['action'] == 'wait':
#         response_text = command['response']
#     elif command['action'] == 'song':
#         response_text = command['response']
#         # тип песня
#
#     return response_text
#
#
# def listen_and_recognize_continuous():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True,
#                     frames_per_buffer=porcupine.frame_length)
#     print("Слушаю...")
#
#     start_time = time.time()
#
#     while True:
#         data = stream.read(porcupine.frame_length)
#         if kaldi_rec.AcceptWaveform(data):
#             result = json.loads(kaldi_rec.Result())
#             user_speech = result.get('text', '')
#             if user_speech:
#                 print(f"user said: {user_speech}")
#
#                 command = find_best_command(user_speech)
#                 if command:
#                     response = execute_command(command)
#                     print(response)
#
#                 start_time = time.time()
#
#         if time.time() - start_time > 7:
#             print("Время ожидания истекло.")
#             break
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
#
# recorder = PvRecorder(device_index=config.MICROPHONE_INDEX, frame_length=porcupine.frame_length)
# recorder.start()
# print('Используемое устройство: %s' % recorder.selected_device)
#
# print(f"Гоша начал свою работу ...")
#
# while True:
#     try:
#         pcm = recorder.read()
#         keyword_index = porcupine.process(pcm)
#
#         if keyword_index >= 0:
#             listen_and_recognize_continuous()
#
#     except KeyboardInterrupt:
#         print("Остановка...")
#         recorder.stop()
#         break