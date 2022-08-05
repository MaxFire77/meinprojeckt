from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import socket
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class MyPopup(FloatLayout):
    pass

def show_popup():
    show = MyPopup()
    popupWindow = Popup(title="Error", content=show, size_hint=(0.6, 0.2))
    popupWindow.open()

class FirstWindow(Screen):
    def callback(self):
        client.sendall(bytes(self.ids.Inp.text, 'UTF-8'))
    def callback2(self):
        client.sendall(bytes("volume-max", 'UTF-8'))
    def callback3(self):
        client.sendall(bytes("error", 'UTF-8'))
    def progress(self):
        text = self.ids.Inp.text

text2 = ""
class SecondWindow(Screen):
    def callback4(self):
        try:
            client.connect((text2, 1234))
        except:
            show_popup()
    def progress2(self):
        global text2
        text2 = self.ids.InpP.text
        return text2


class ThirdWindow(Screen):
    def callback5(self):
        client.sendall(bytes("DELETE-exe", 'UTF-8'))

class WindowManager(ScreenManager):
    pass

class MyBL(BoxLayout):
    pass


kv_file = Builder.load_file('KV.kv')

class Applicatte(App):
    running = True
    def build(self):
        return kv_file
    def on_stop(self):
        self.running = False

if __name__ == '__main__':
    Applicatte().run()
