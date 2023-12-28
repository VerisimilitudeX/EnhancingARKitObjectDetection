import cv2
import shutil
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

def is_blurry(image_path, threshold=100):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return None
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    variance = laplacian.var()
    return variance < threshold

def detect_and_move_non_blurry_images(folder_path, threshold=7):
    # Create a new folder for non-blurry images
    non_blurry_folder = os.path.join(folder_path, "non_blurry")
    if not os.path.exists(non_blurry_folder):
        os.makedirs(non_blurry_folder)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        blur_status = is_blurry(file_path, threshold)
        if blur_status is None:
            print(f"Failed to load image: {file_path}")
            continue

        # If the image is not blurry, move it to the new folder
        if not blur_status:
            shutil.move(file_path, os.path.join(non_blurry_folder, filename))

# Usage
folder_path = "C:\\Users\\achar\\OneDrive\\Documents\\GitHub\\EnhancingARKitObjectDetection\\Process\\frames"
detect_and_move_non_blurry_images(folder_path)
