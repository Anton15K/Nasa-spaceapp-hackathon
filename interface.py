from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.app import App
import os
# Import the "run" function from the "video_resolve" module
from video_resolve import run as video_resolve
# Import the "result_video" function from the "run_video" module
from run_video import result_video as run_video

sp = os.path.sep
class Main(Screen):
    # Define the "get_name" method, which is called when the "Add Video" button is pressed
    def get_name(self, vid):
        # Clear the text of the "vid" TextInput widget
        self.ids.vid.text = ""
        try:
            # Call the "run" function from the "video_resolve" module to resolve the video file
            video_resolve(f"videos{sp}{vid}")
            # Update the hint text of the "vid" TextInput widget to indicate that the video was added successfully
            self.ids.vid.hint_text = "Video was added to load, click load_image to continue"
        except:
            # Update the hint text of the "vid" TextInput widget to indicate that an error occurred
            self.ids.vid.hint_text = "Error, try again"
            
    # Define the "play_video" method, which is called when the "Load Image" button is pressed
    def play_video(self):
        # Call the "result_video" function from the "run_video" module to play the video file
        run_video()
        

# Create a ScreenManager object
sm = ScreenManager()
# Add a Main screen to the ScreenManager
sm.add_widget(Main(name="main"))

# Define the "MyApp" class, which inherits from the "App" class in Kivy
class MyApp(App):
    # Define the "build" method, which is called when the app is launched
    def build(self):
        # Load the "APP.kv" file and return the root widget
        screen = Builder.load_file("APP.kv")
        return screen


if __name__ == '__main__':
    MyApp().run()


