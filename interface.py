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
from kivy.uix.videoplayer import VideoPlayer

from moviepy.editor import *
import cv2
import os
#import video_resolve
sp = os.path.sep

class Main(Screen):
    def get_name(self, vid):
        self.ids.vid.text = ""
        try:
            with open("path.txt", "w") as f:
                f.write(vid)
            self.ids.vid.hint_text = "Video was added to load, click load_image to continue"
            #video_resolve.show_video(vid)
        except:
            self.ids.vid.hint_text = "Something went wrong"
    def play_video(self):
        with open("path.txt", "r") as f:
            path = f.read()
            clip = VideoFileClip(f"images{sp}{path}")
            clip.preview(fps = 30)




sm = ScreenManager()
sm.add_widget(Main(name="main"))




class MyApp(App):
    def build(self):
        screen = Builder.load_file("APP.kv")
        return screen




if __name__ == '__main__':
    MyApp().run()


