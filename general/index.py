import datetime
import json
from fuzzywuzzy import fuzz
import tts
from num2words import num2words
import voice_detection
import stt
import pathlib
from pathlib import Path
import torch

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'json_files', 'commands.json')

# Проверка наличия файла
if not path.exists():
    print(f"Файл {path} не найден!")
    exit()

# Открытие файла с указанием кодировки UTF-8
with open(fr'{path}', 'r', encoding='utf-8') as file:
    commands_data = json.load(file)
    commands = commands_data.get('commands', [])
    if not commands:
        print("Команды не найдены в файле commands.json")
        exit()





def command_filter(user_speech):
    print(f"Пользователь сказал: {user_speech}")
    best_command = None
    max_ratio = 0

    for command in commands:
        activation_phrase = command['activation_phrase']
        ratio = fuzz.ratio(user_speech, activation_phrase)
        print(f"Сравнение с '{activation_phrase}': {ratio}%")

        if ratio > max_ratio:
            max_ratio = ratio
            best_command = command

    if best_command and max_ratio > 10:
        print(f"Лучшая команда: {best_command['activation_phrase']} с коэффициентом {max_ratio}")
        return best_command
    else:
        print("Команда не найдена или низкий коэффициент сходства.")
    return None

def processingCommands(command):
    if command['action'] == 'time':
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
        response_text = f"{command['response']} {text}"
    elif command['action'] == 'hello':
        response_text = f"{command['response']}"
    else:
        response_text = "Неизвестная команда"
    return response_text

def listen_and_responce():
    print('Слушаю...')
    while True:
        speech = stt.Recognition()
        print(f"Распознанная речь: {speech}")

        command = command_filter(speech)
        if command:
            print(f"Найденная команда: {command}")
            response = processingCommands(command)
            print(f"Ответ: {response}")
            tts.Checking_the_connection(response)
            key_word_detect()
        else:
            print("Команда не найдена.")

def key_word_detect():
    print('VH Слушает...')
    while True:
        keyWord = voice_detection.callback(False)
        if keyWord:
            print('Ключевое слово сработало!!!')
            listen_and_responce()

def loadind_models():
    # Загрузка модели Vosk
    stt.load_model()

    # Загрузка модели Silero
    language = 'ru'
    model_id = 'v4_ru'
    device = torch.device('cpu')  # Используем CPU для загрузки модели
    model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                         model='silero_tts',
                                         language=language,
                                         speaker=model_id)
    model.to(device)
    key_word_detect()

loadind_models()










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


