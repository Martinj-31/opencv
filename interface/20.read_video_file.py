# Import necessary libraries
import cv2
import numpy as np
import os
import urllib.request

# Function to apply Gaussian blur to an image
def apply_blur(img, k):
    """Apply Gaussian blur to the entire image."""
    return cv2.GaussianBlur(img, (k, k), 0)

# Function to pixelate a specific region in an image
def pixelate_region(image, startX, startY, endX, endY):
    """Pixelate a specific region in the image."""
    region = image[startY:endY, startX:endX]
    h, w = region.shape[:2]
    temp = cv2.resize(region, (10, 10), interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
    image[startY:endY, startX:endX] = pixelated
    return image

# Function to pixelate the face in an image
def pixelate_face(image, blocks=10):
    """Detect faces, pixelate them, and draw rectangles around detected faces."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        # Pixelate the detected face region
        image = pixelate_region(image, x, y, x + w, y + h)
        # Draw a rectangle around the detected face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

# Function to download the Haarcascade file if not exists
def download_haarcascade_file():
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml'
    filename = 'haarcascade_frontalface_default.xml'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully.")

if __name__ == "__main__":
    # Download Haarcascade file if not exists
    download_haarcascade_file()

    # Load the Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Capture video stream and apply pixelation to detected faces
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        exit()

    print("Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from the webcam.")
            break

        # Pixelate faces in the frame and draw rectangles
        pixelated_frame = pixelate_face(frame)

        # Display the result
        cv2.imshow('Pixelated Faces', pixelated_frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
