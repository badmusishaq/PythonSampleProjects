import cv2

img = cv2.imread('galaxy.jpg', 0)  # Load an image from file

#resized_image = cv2.resize(img, (400, 600))  # Resize the image to 400x300 pixels
resized_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))  # Resize the image to half its original size


cv2.imshow('Galaxy', resized_image)  # Display the image in a window

cv2.imwrite('resized_galaxy.jpg', resized_image)  # Save the resized image to a new file
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all windows
