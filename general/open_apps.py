import os
import subprocess
import time
import psutil
from screeninfo import get_monitors


def get_secondary_monitor():
    monitors = get_monitors()
    if len(monitors) > 1:
        return monitors[1]  # Возвращаем второй монитор
    return None


def find_window_by_process_name(process_name):
    # Ищем процесс по имени
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            pid = proc.info['pid']
            # Получаем список окон для процесса
            windows = get_windows_for_process(pid)
            for window in windows:
                return window
    return None


def get_windows_for_process(pid):
    windows = []
    try:
        import pygetwindow as gw
        for window in gw.getAllWindows():
            if window._hWnd == gw.win32functions.GetWindowThreadProcessId(window._hWnd)[1]:
                if pid == gw.win32functions.GetWindowThreadProcessId(window._hWnd)[1]:
                    windows.append(window)
    except ImportError:
        pass
    return windows


def move_window_to_secondary_monitor(window):
    # Получаем координаты второго монитора
    secondary_monitor = get_secondary_monitor()
    if not secondary_monitor:
        print("Второй монитор не найден")
        return

    # Перемещаем окно на второй монитор
    window.moveTo(secondary_monitor.x, secondary_monitor.y)


def open_item(item_path):
    if os.path.isdir(item_path):
        # Открываем папку
        subprocess.Popen(['explorer', item_path])
        time.sleep(2)  # Даем проводнику время на открытие папки
        window_title = os.path.basename(os.path.normpath(item_path))
    elif os.path.isfile(item_path):
        # Открываем файл (например, приложение)
        subprocess.Popen([item_path])
        time.sleep(5)  # Даем приложению время на открытие
        window_title = os.path.basename(item_path)
    else:
        print(f"Элемент по пути {item_path} не найден")
        return

    process_name = os.path.basename(item_path)
    window = find_window_by_process_name(process_name)
    if window:
        move_window_to_secondary_monitor(window)
    else:
        print(f"Окно с процессом, содержащим '{process_name}', не найдено")


# Пример использования
item_path = input("Введите путь к приложению или папке: ")  # Укажите путь к приложению или папке
open_item(item_path)
