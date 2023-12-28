import cv2
import os

pathtovideo = input("Enter the path to the video file: ")
cap = cv2.VideoCapture(pathtovideo)
count = 0
# create a folder named 'frames' next to the video file
folder = os.path.join(os.path.dirname(pathtovideo), 'frames')
os.makedirs(folder, exist_ok=True)
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break # exit the loop if no more frames
    # save each frame as an image file in the 'frames' folder
    cv2.imwrite(os.path.join(folder, "frame%d.jpg" % count), frame)
    count = count + 1
cap.release()