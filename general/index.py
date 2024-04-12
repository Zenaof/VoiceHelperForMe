import datetime
import json
from fuzzywuzzy import fuzz
import tts
from num2words import num2words
import voice_detection
import stt
import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'commands.json')

with open(fr'{path}', 'r') as file:
    commands_data = json.load(file)
    commands = commands_data.get('commands', [])

def command_filter(user_speech):
    best_command = None
    max_ratio = 0

    for command in commands:
        activation_phrase = command['activation_phrase']
        # проверяем сходство того что сказал пользователь и активационной фразы
        ratio = fuzz.ratio(user_speech, activation_phrase)
        if ratio > max_ratio:
            max_ratio = ratio
            best_command = command
        if best_command and max_ratio > 10:
            return best_command

def processingCommands(command):
    if command['action'] == 'time':
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
        responce_text = f"{command['response']} {text}"
    elif command['action'] == 'hello':
        responce_text = f"{command['response']}"
    return responce_text




def listen_and_responce():
    print('Слушаю...')
    while True:
        speech = stt.Recognition()
        print(speech)

        command = command_filter(speech)
        if command:
            response = processingCommands(command)
            tts.Checking_the_connection(response)
            key_word_detect()



def key_word_detect():
    print('VH Слушает...')
    while True:
        keyWord = voice_detection.callback(False)
        if keyWord == True:
            print('ключевое слово сработало!!!')
            listen_and_responce()

key_word_detect()










# def start_VH(voice):
#     print(voice)
#
#
# def filter_cmd(initial_voice):
#     cmd = initial_voice
#     for x in config.VA_TBR:
#         cmd = cmd.replace(x, "").strip()
#
#     return cmd
#
# def recognize_cmd(cmd: str):
#     rc = {'cmd': '', 'percent': 0}
#     for c, v in config.VH_CMD_LIST.items():
#
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > rc['percent']:
#                 rc['cmd'] = c
#                 rc['percent'] = vrt
#
#     return rc
#
# def commandCheck(voice):
#     commands_list = config.VH_CMD_LIST.keys()
#     cmd = recognize_cmd(filter_cmd(voice))
#     print(voice)
#     if cmd['cmd'] in commands_list:
#         # Если то что сказал пользователь есть в списке команд
#         processingCommands(voice)
#     else:
#         tts.Checking_the_connection("Простите я не знаю такой комманды")
#
# def processingCommands(cmd: str):
#     if cmd == 'help':
#         text = "Я умею: ..."
#         text += "говорить местоположение транспорта ..."
#         text += "и открывать браузер"
#         tts.va_speak(text)
#         pass


