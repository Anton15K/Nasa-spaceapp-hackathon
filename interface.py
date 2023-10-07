import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.logger import logging
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video
import os
#import video_resolve
sp = os.path.sep

class Main(Screen):
    def get_name(self, img):
        self.ids.img.text = ""
        try:
            with open("path.txt", "w") as f:
                f.write(img)
            self.ids.img.hint_text = "Image was added to load, click load_image to continue"
            #video_resolve.show_video(img)
        except:
            self.ids.img.hint_text = "Something went wrong"


sm = ScreenManager()
sm.add_widget(Main(name="main"))



class MyApp(App):
    def build(self):
        screen = Builder.load_file("APP.kv")
        return screen




if __name__ == '__main__':
    MyApp().run()


