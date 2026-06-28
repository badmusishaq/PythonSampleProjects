import cv2

face_cascade = cv2.CascadeClassifier('FaceDetector/haarcascade_frontalface_default.xml')

img = cv2.imread('FaceDetector/news.jpg')  # Load an image from folder
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)  # Detect faces in the image

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around each detected face

resized_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))  # Resize the image to half its original size

cv2.imshow('Image with Faces', resized_image)  # Display the resized image with detected faces in a window
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all windows