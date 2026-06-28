import cv2

first_frame = None  # Initialize the first frame variable

video = cv2.VideoCapture(0)  # Open the default camera (0)

while True:
    check, frame = video.read()  # Read a frame from the camera
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # Apply Gaussian blur to the grayscale frame


    if first_frame is None:
        first_frame = gray_frame  # Set the first frame to the current grayscale frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)  # Compute the absolute difference between the first frame and the current frame
    #thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]  # Apply a binary threshold to the delta frame
    #thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #cv2.imshow("Capturing", frame)  # Display the captured frame in a window
    cv2.imshow("Gray Frame", gray_frame)  # Display the captured grayscale frame in a window
    cv2.imshow("Delta Frame", delta_frame)  # Display the delta frame in a window

    key = cv2.waitKey(1)  # Wait for a key press to close the window

    if key == ord('q'):  # If the 'q' key is pressed, exit the loop
        break

video.release()  # Release the camera resource
cv2.destroyAllWindows()  # Close all windows