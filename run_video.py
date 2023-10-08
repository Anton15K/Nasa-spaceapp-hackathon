
import combine_video
import os
def result_video():
    sp = os.path.sep
    sounds = f"sounds{sp}out.wav"
    video_name = f"videos{sp}output.mp4"
    combine_video.combine(video_name, sounds)
