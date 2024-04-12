import pvporcupine
import voice_detection
import os
import pathlib
from pathlib import Path

keywords_path = 'Hey-Yuki-windows.ppn'
if os.name == 'posix':
    keywords_path = 'Hey-Yuki-linux.ppn'

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'new-model', 'picovoice-models', f'{keywords_path}')

access_key = 'ixVF5hzgPK+0NUVXWFDW1FKDUPsNTjnd7IRg3vtD3Qic1dxz8UQxgQ=='
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[fr'{path}'])
