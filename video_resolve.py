import cv2
import numpy as np
import wavio
import time
import random
import os
import math



# Constants
RATE = 44100  # Sample rate (samples/second)
AMPLITUDE = 1  # Constant amplitude
FADE_DURATION = 0.1  # 100ms fade in and fade out


audio_data = []
brightnesses = []

# C4 Major Scale Frequencies
C4_MAJOR_SCALE = [49.7, 66.3, 83.5, 88.5, 111.5, 118.1, 125.1, 140.3, 140.5, 148.8, 157.7, 167.0, 187.5, 198.6, 210.5, 223.0, 250.3, 265.2, 280.9, 297.6, 315.3, 334.1, 354.0, 375.0, 420.9, 446.0, 472.5, 500.6, 561.9]
C4_MAJOR_SCALE = sorted(C4_MAJOR_SCALE)
previous_sounds = []
def create_video(out):
    pass
def process_lines(result, line, frame):
    sz = len(line)
    average_r = 0
    average_g = 0
    average_b = 0
    for el in line:
        x, y = el
        #print(frame[y, x])
        R, G, B = frame[y, x]
        average_r += R
        average_g += G
        average_b += B
    average_r //= sz
    average_g //= sz
    average_b //= sz
    result[0] += average_r
    result[1] += average_g
    result[2] += average_b
    #print(average_r, average_g, average_b)
    return result
def convert_to_sound(pixels_to_convert):
    print(pixels_to_convert)
    red, green, blue = pixels_to_convert  # get pixel RGB value
    luminosity = (red + green + blue) // 3 # calculate brightness
    # Print the luminosity value
    print(luminosity)

    # Calculate the index of the note to play based on the luminosity value
    index = ((luminosity + 50) % 256) // 9

    # Check if the previous three notes played were the same, and if so, increment the index
    if len(previous_sounds) > 2:
        if previous_sounds[-1] == index and previous_sounds[-2] == index and previous_sounds[-3] == index:
            index += 1
            index %= len(C4_MAJOR_SCALE)

    # Add the index to the list of previous notes played
    previous_sounds.append(index)

    # Calculate the frequency of the note to play
    freq = C4_MAJOR_SCALE[index]

    # Calculate a duration so that the waveform ends near a zero crossing
    samples_per_wave = RATE / freq
    total_samples = int(samples_per_wave * np.round(RATE * 1 / samples_per_wave))

    # Generate a sine wave with the calculated frequency and duration
    t = np.linspace(0, total_samples / RATE, total_samples, endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)

    # Apply a fade-in and fade-out to the waveform
    fade_in = np.linspace(0, 1, int(FADE_DURATION * RATE))
    fade_out = np.linspace(1, 0, int(FADE_DURATION * RATE))
    fade = np.ones_like(signal)
    fade[:len(fade_in)] = fade_in
    fade[-len(fade_out):] = fade_out
    signal *= fade

    # Apply the desired amplitude to the waveform
    signal *= AMPLITUDE

    # Add the waveform to the list of audio data
    audio_data.append(signal)

    # Define a function to generate a list of pixels along a line between two points using Bresenham's line algorithm
    def bresenham_line(x0, y0, x1, y1):
        result = []
        for i in range(x0, x1 + 1):
            result.append((i, y0))
            if y0 != y1:
                result.append((i, y1))
        for i in range(y0 + 1, y1):
            result.append((x0, i))
            if x0 != x1:
                result.append((x1, i))
        return result

    # Define a function to process the pixels along a line and update the average color for the frame
    def process_lines(average_colour_for_frame, line, frame):
        for x, y in line:
            average_colour_for_frame[0] += frame[y, x, 0]
            average_colour_for_frame[1] += frame[y, x, 1]
            average_colour_for_frame[2] += frame[y, x, 2]

    # Define a function to resolve a video file into audio and visual components
    def resolve_video(video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Get the dimensions of the video frames
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create an empty numpy ndarray to hold the video frames
        video_array = np.empty((frame_count, frame_height, frame_width, 3), dtype=np.uint8)

        # Loop through each frame in the video and add it to the numpy ndarray
        for i in range(frame_count):
            ret, frame = cap.read()
            if ret:
                video_array[i] = frame
            else:
                break

        # Release the video capture object
        cap.release()

        # Assuming that you have already loaded the video_array ndarray
        num_frames, frame_height, frame_width, _ = video_array.shape

        # Calculate the center point of the ndarray
        center_x = frame_width // 2
        center_y = frame_height // 2
        center_point = (center_x, center_y)

        print("Center point:", center_point)

        # Define the color of the lines to draw
        R_colour = 0
        G_colour = 255
        B_colour = 0

        # Define some variables for processing the video frames
        coord = 0
        sz = frame_height + frame_width
        c = sz // frame_count + 1
        print(frame_count, sz, c, fps)

        average_colour_for_second = [0, 0, 0]
        number_of_used_lines = 0
        a = 0
        gcd_height_width = math.gcd(frame_height, frame_width)
        deltax = frame_width // gcd_height_width
        deltay = frame_height // gcd_height_width

        # Loop through each frame in the video array and draw lines on the frame
        sp = os.path.sep
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter(f'videos{sp}output.mp4', fourcc, 30.0, (frame_width, frame_height))
        for frame in video_array:
            number_of_used_lines += 1
            average_colour_for_frame = [0, 0, 0]
            for i in range(c):
                # Draw a line from the center point to each corner pixel of the frame
                x0 = coord * deltax
                y0 = coord * deltay
                x1 = frame_width-coord * deltax -1
                y1 = frame_height - coord * deltay - 1
                process_lines(average_colour_for_frame, bresenham_line(x0, y0, x1, y1), frame)
                cv2.rectangle(frame, (x0, y0), (x1, y1), (R_colour, G_colour, B_colour), 1)

            # Update the average color for the second
            average_colour_for_second[0] += average_colour_for_frame[0] // c
            average_colour_for_second[1] += average_colour_for_frame[1] // c
            average_colour_for_second[2] += average_colour_for_frame[2] // c

            # Update the coordinate for the next set of lines to draw
            coord += 1
            coord %= (frame_height // 2 // deltay)

            # If a second has passed, convert the average color to a sound and reset the average color
            if number_of_used_lines % fps == 0:
                average_colour_for_second[0] //= fps
                average_colour_for_second[1] //= fps
                average_colour_for_second[2] //= fps
                convert_to_sound(average_colour_for_second)
                average_colour_for_second = [0, 0, 0]
                a += 1

            # Write the frame to the output video file
            out.write(frame)

        # Release the VideoWriter object
        out.release()

        # Concatenate all the small signals into one signal
        global audio_data
        audio_data = np.hstack(audio_data)

        # Normalize the audio data to 16-bit PCM
        audio_data = (audio_data * (2 ** 15 - 1)).astype(np.int16)

        # Save the audio data to a .wav file
        wavio.write("sounds/out.wav", audio_data, RATE)

    # Define a function to run the video resolution process
    def run(video_path):
        resolve_video(video_path)
