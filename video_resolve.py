import cv2
import numpy as np
import time

##### define  musical parameters
scale = MIXOLYDIAN_SCALE

minPitch = 0  # MIDI pitch (0-127)
maxPitch = 127

minDuration = 0.8  # duration (1.0 is QN)
maxDuration = 6.0

minVolume = 0  # MIDI velocity (0-127)
maxVolume = 127
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
    #print(pixels_to_convert)
    red, green, blue = pixels_to_convert  # get pixel RGB value

    luminosity = (red + green + blue) / 3  # calculate brightness

    # map luminosity to pitch (the brighter the pixel, the higher
    # the pitch) using specified scale
    pitch = mapScale(luminosity, 0, 255, minPitch, maxPitch, scale)

    # map red value to duration (the redder the pixel, the longer
    # the note)
    #duration = mapValue(red, 0, 255, minDuration, maxDuration)

    # map blue value to dynamic (the bluer the pixel, the louder
    # the note)
    #dynamic = mapValue(blue, 0, 255, minVolume, maxVolume)

    # create note and return it to caller
    #note = Note(pitch, duration, dynamic)

    # done sonifying this pixel, so return result'''
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    result = []
    while x0 != x1 or y0 != y1:
        result.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    result.append((x1, y1))
    return result
def resolve_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Get the number of frames in the video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the dimensions of the video frames
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create an empty numpy ndarray to hold the video frames
    video_array = np.empty((num_frames, frame_height, frame_width, 3), dtype=np.uint8)

    # Loop through each frame in the video and add it to the numpy ndarray
    for i in range(num_frames):
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
    # line colour parametres
    R_colour = 0
    G_colour = 255
    B_colour = 0

    prev_x = 0
    prev_y = 0

    sz = frame_height + frame_width
    c = sz // frame_count + 1
    print(frame_count, sz, c, fps)

    average_colour_for_second = [0, 0, 0]
    number_of_used_lines = 0
    a = 0
    if 0 == 1:
        pass
        #c = frame_count // sz
    # Loop through each frame in the video array and draw a circle on the center pixel
    else:
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (frame_width, frame_height))
        for frame in video_array:
            number_of_used_lines += 1
            average_colour_for_frame = [0, 0, 0]
            for i in range(prev_x, min(prev_x + c, frame_width)):
            # Draw a circle on the center pixel of the frame
                #cv2.circle(frame, center_point, 1, (0, 0, 255), -1)

                # Draw a line from the center point to each corner pixel of the frame
                x0 = i
                y0 = frame_height - 1
                x1 = frame_width-i-1
                y1 = 0
                process_lines(average_colour_for_frame, bresenham_line(x0, y0, x1, y1), frame)
                cv2.line(frame, (x0, y0), (x1, y1), (R_colour, G_colour, B_colour), 1)
                '''or el in bresenham_line(x0, y0, x1, y1):
                    print(el[0], el[1])'''
                '''cv2.imshow("Frame", frame)
                cv2.waitKey(1000//30)'''
            average_colour_for_second[0] += average_colour_for_frame[0] // c
            average_colour_for_second[1] += average_colour_for_frame[1] // c
            average_colour_for_second[2] += average_colour_for_frame[2] // c
            prev_x += c
            if prev_x < frame_width:
                '''cv2.imshow("Frame", frame)
                cv2.waitKey(1000//fps)'''
                if number_of_used_lines % fps == 0:
                    average_colour_for_second[0] //= fps
                    average_colour_for_second[1] //= fps
                    average_colour_for_second[2] //= fps
                    print(number_of_used_lines)
                    convert_to_sound(average_colour_for_second)
                    average_colour_for_second = [0, 0, 0]
                    a += 1
                out.write(frame)
                continue
            for i in range(prev_y, min(prev_y + c, frame_height)):
                x0 = frame_width - 1
                y0 = frame_height - i - 1
                x1 = 0
                y1 = i
                process_lines(average_colour_for_frame, bresenham_line(x0, y0, x1, y1), frame)
                cv2.line(frame, (x0, y0), (x1, y1), (R_colour, G_colour, B_colour), 1)
                #cv2.line(frame, center_point, (center_x-i, 0), (0, 0, 0), 1)
            average_colour_for_second[0] += average_colour_for_frame[0] // c
            average_colour_for_second[1] += average_colour_for_frame[1] // c
            average_colour_for_second[2] += average_colour_for_frame[2] // c
            if number_of_used_lines % fps == 0:
                average_colour_for_second[0] //= fps
                average_colour_for_second[1] //= fps
                average_colour_for_second[2] //= fps
                print(number_of_used_lines)
                convert_to_sound(average_colour_for_second)
                average_colour_for_second = [0, 0, 0]
                a += 1
            '''cv2.imshow("Frame", frame)
            cv2.waitKey(1000//fps)'''
            out.write(frame)

            # Release the VideoWriter object

            # Print the output video path
            

            prev_y += c
            if prev_y < frame_height:
                continue
            else:
                prev_x = 0
                prev_y = 0
        print(a)
        out.release()

resolve_video("images/Hydra.mp4")