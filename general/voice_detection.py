import pathlib
import time
from pvrecorder import PvRecorder
import os
from pathlib import Path
from configVH import porcupine

recorder = PvRecorder(frame_length=porcupine.frame_length)
recorder.start()
print('Используемое устройство: %s' % recorder.selected_device)

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

# print('VH Слушает...')
# while True:
#     keyWord = callback(False)
#     if keyWord == True:
#         print('ключевое слово сработало!!!')
