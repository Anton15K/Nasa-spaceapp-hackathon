import combine_sound
import combine_video

def result_video():
    sounds = get_sounds()
    video_name = get_video()
    combine_sound(sounds)
    combine_video(video_name, "combined.mp3")