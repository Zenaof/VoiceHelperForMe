import pvporcupine
import sounddevice as sd
import numpy as np
import time
from pvrecorder import PvRecorder


#Настройка Porcupine
access_key = 'ixVF5hzgPK+0NUVXWFDW1FKDUPsNTjnd7IRg3vtD3Qic1dxz8UQxgQ=='
keywords_path = '../new-model/picovoice-models/Hey--Yuki_en_linux_v3_0_0/Hey-Yuki-linux.ppn'

porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[keywords_path])
recorder = PvRecorder(device_index=1, frame_length=porcupine.frame_length)
recorder.start()
print('Используемое устройство: %s' % recorder.selected_device)

def nextFrame(keyWord):
    print('Сработала функция', keyWord)


def callback(keyWord):
    while True:
        try:
            pcm = recorder.read()
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                keyWord = True
                return keyWord
                time.sleep(0.3)
                keyWord = False
        except:
            print('stop')
            recorder.stop()
            break
    porcupine.delete()