import pyaudio
import vosk
import sys
import sounddevice as sd
import queue
import json
import pyaudio
import voice_detection

model = vosk.Model(r"../new-model/vosk-model-ru-0.22") # полный путь к модели
samplerate = 16000
device = 1
porcupine = voice_detection.porcupine
kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
def Recognition():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=porcupine.frame_length)

    while True:
        data = stream.read(porcupine.frame_length)
        if kaldi_rec.AcceptWaveform(data):
            result = json.loads(kaldi_rec.Result())
            user_speech = result.get('text', '')
            return user_speech


























q = queue.Queue()
# def q_callback(indata, frames, time, status):
#     if status:
#         print(status, file=sys.stderr)
#     q.put(bytes(indata))
#
# def Recogition(callback):
#     with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
#                            channels=1, callback=q_callback):
#
#         rec = vosk.KaldiRecognizer(model, samplerate)
#         while True:
#             data = q.get()
#             if rec.AcceptWaveform(data):
#                 callback(json.loads(rec.Result())["text"])
#             #else:
#             #    print(rec.PartialResult())