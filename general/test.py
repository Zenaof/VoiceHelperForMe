from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Window.clearcolor = 0, 1, 1, 1


class RegisterPage(Screen):
    pass


class LoginPage(Screen):
    pass


class MainPage(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class VHApp(App):
    def build(self):
        return

kv = Builder.load_file('VHApp.kv')

if __name__ == '__main__':
    VHApp().run()
