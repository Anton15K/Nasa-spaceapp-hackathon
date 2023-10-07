import cv2
import numpy as np
import time


def create_video(out):
    pass

def convert_to_sound(pixels_to_convert):
    pass

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
    print(frame_count, sz, c)
    if 0 == 1:
        pass
        #c = frame_count // sz
    # Loop through each frame in the video array and draw a circle on the center pixel
    else:
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (frame_width, frame_height))
        for frame in video_array:
            for i in range(prev_x, min(prev_x + c, frame_width)):
            # Draw a circle on the center pixel of the frame
                #cv2.circle(frame, center_point, 1, (0, 0, 255), -1)

                # Draw a line from the center point to each corner pixel of the frame
                cv2.line(frame, (i, frame_height), (frame_width-i, 0), (R_colour, G_colour, B_colour), 1)
                convert_to_sound(bresenham_line(i, frame_height, frame_width-i, 0))
                '''cv2.imshow("Frame", frame)
                cv2.waitKey(1000//30)'''

            prev_x += c
            if prev_x < frame_width:
                '''cv2.imshow("Frame", frame)
                cv2.waitKey(1000//fps)'''
                out.write(frame)
                
                continue
            for i in range(prev_y, min(prev_y + c, frame_height)):
                cv2.line(frame, (frame_width, frame_height-i), (0, 0+i), (R_colour, G_colour, B_colour), 1)
                #cv2.line(frame, center_point, (center_x-i, 0), (0, 0, 0), 1)

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
        out.release()




print(resolve_video("images/saturn.mp4"))


