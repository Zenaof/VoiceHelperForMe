import pathlib
import vosk
import json
import pyaudio
import config
from pathlib import Path

# Выбор можели воск маленькая или большая
modelVoskLarge = False
if modelVoskLarge == True:
    modelVosk = 'vosk-model-large'
else:
    modelVosk = 'vosk-model-small'


dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'new-model', 'vosk-models', f'{modelVosk}')

model = vosk.Model(fr'{path}') # полный путь к модели
samplerate = 16000
device = 1
porcupine = config.porcupine
kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
def Recognition():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=config.porcupine.frame_length)

    while True:
        data = stream.read(porcupine.frame_length)
        if kaldi_rec.AcceptWaveform(data):
            result = json.loads(kaldi_rec.Result())
            user_speech = result.get('text', '')
            return user_speech
