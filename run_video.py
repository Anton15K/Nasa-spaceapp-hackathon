# import the combine_video module
import combine_video

# import the os module
import os

# define the result_video function
def result_video():
    # set the separator for the current operating system
    sp = os.path.sep

    # set the path for the output sound file
    sounds = f"sounds{sp}out.wav"

    # set the path for the output video file
    video_name = f"videos{sp}output.mp4"

    # call the combine function from the combine_video module to combine the sound and video files
    combine_video.combine(video_name, sounds)
