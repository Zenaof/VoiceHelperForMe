import pvporcupine
import os
import pathlib
from pathlib import Path

# keywords_path = 'Hey-Yuki-windows.ppn'
# if os.name == 'posix':
#     keywords_path = 'Hey-Yuki-linux.ppn'
#
# dir_path = pathlib.Path.cwd()
# path = Path(dir_path, 'new-model', 'picovoice-models', f'{keywords_path}')
#
# access_key = 'ixVF5hzgPK+0NUVXWFDW1FKDUPsNTjnd7IRg3vtD3Qic1dxz8UQxgQ=='
# picovoi = pvporcupine.create(access_key=access_key, keyword_paths=[str(Path)])

# keywords_path = 'file.ppn'
# dir_path = pathlib.Path.cwd()
# path = Path(dir_path, 'new-model', 'picovoice-models', keywords_path)

# if not path.is_file():
#     raise FileNotFoundError(f"Keyword file not found at {path}")
#
# print(f"-------------------------------------------------------: {path}")
path_file = 'C:/Users/user/PycharmProjects/VoiceHelperForMe/general/new-model/picovoice-models/Hey-Yuki-windows.ppn'
# Ключ доступа
access_key = 'GSpl0S6dwNH2M2ZV5siJW1CKkfBYYTLnUkX1xUrpvRVFm8Nsrnx4bA=='

try:
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[str(path_file)]
    )
except pvporcupine.PorcupineActivationLimitError:
    print("Activation limit exceeded for the provided access key.")
    # Дополнительные действия по обработке ошибки
except Exception as e:
    print(f"An error occurred: {e}")
    # Обработка других возможных ошибок