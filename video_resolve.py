import cv2
import numpy as np
import time
def resolve_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

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
    i = 0
    # Loop through each frame in the video array and draw a circle on the center pixel
    for frame in video_array:
        for i in range(center_x):
        # Draw a circle on the center pixel of the frame
            cv2.circle(frame, center_point, 1, (0, 0, 255), -1)

            # Draw a line from the center point to each corner pixel of the frame
            cv2.line(frame, center_point, (center_x-i, 0), (0, 255, 0), 1)
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)
        for i in range(center_y):
            cv2.line(frame, center_point, (0, 0+i), (0, 255, 0), 1)
            
            #cv2.line(frame, center_point, (center_x-i, 0), (0, 0, 0), 1)
        
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)
        

    return video_array


def show_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

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
    i = 0
    # Loop through each frame in the video array and draw a circle on the center pixel
    for frame in video_array:
        for i in range(center_x):
        # Draw a circle on the center pixel of the frame
            cv2.circle(frame, center_point, 1, (0, 0, 255), -1)

            # Draw a line from the center point to each corner pixel of the frame
            cv2.line(frame, center_point, (center_x-i, 0), (0, 255, 0), 1)
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)
        for i in range(center_y):
            cv2.line(frame, center_point, (0, 0+i), (0, 255, 0), 1)
        
            #cv2.line(frame, center_point, (center_x-i, 0), (0, 0, 0), 1)
        
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)
        

    return video_array
print(resolve_video("images/saturn.mp4"))
