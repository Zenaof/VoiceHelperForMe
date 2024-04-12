import time
import requests
import torch
import silero
import sounddevice as sd


def Conversator_Offline(text):
    language = 'ru'
    model_id = 'v4_ru'
    device = torch.device('cpu')
    sample_rate = 48000
    speaker = 'baya' #kseniya, xenia, aidar, baya
    put_accent = True
    put_yo = True
    example_text = text

    model, exaple_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                        model='silero_tts',
                                        language=language,
                                        speaker=model_id)
    model.to(device)

    audio = model.apply_tts(text=example_text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    #Воспроизводим текст
    print(example_text)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop

def Conversator_Online():
    pass
def Checking_the_connection(text):
    if requests.get('http://ya.ru').ok:
        print('Подключение к интернету присутствует. Запускаю Онлайн версию синтеза речи')
        Conversator_Offline(text)
    else:
        print('Подлючение к интернету отсутствует. Запускаю Оффлайн версию синтеза речи')
        Conversator_Offline(text)

