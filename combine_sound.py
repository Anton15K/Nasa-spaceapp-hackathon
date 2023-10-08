from moviepy.editor import concatenate_audioclips, AudioFileClip
import os
def concatenate_audio_moviepy(audio_clip_paths):
    sp = os.path.sep
    directory = f"mp3{sp}"
    clips = [AudioFileClip(f"{directory}{c}") for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile("combine.mp3")





