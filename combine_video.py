from moviepy.editor import VideoFileClip, AudioFileClip
import os
# Load the video and audio files

def combine(vid, music):
    sp = os.path.sep
    video = VideoFileClip(f"{vid}")
    audio = AudioFileClip(f"{music}")

    # Set the audio of the video file to the loaded audio file
    video = video.set_audio(audio)

    # Write the combined video file to disk
    video.write_videofile("combined.mp4", codec="libx264")
