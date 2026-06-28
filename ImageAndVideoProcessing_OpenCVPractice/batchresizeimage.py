import cv2
import os

#load images in the sample image folder
image_folder = 'sample_images/'
resized_images_folder = 'batch_resized_images/'

# Create the resized images folder if it doesn't exist
os.makedirs(resized_images_folder, exist_ok=True)

for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img = cv2.imread(os.path.join(image_folder, filename), 0)  # Load an image from file
        resized_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))  # Resize the image to half its original size
        cv2.imshow(f'Resized {filename}', resized_image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()  # Close all windows

        cv2.imwrite(os.path.join(resized_images_folder, f"resized_{filename}"), resized_image)