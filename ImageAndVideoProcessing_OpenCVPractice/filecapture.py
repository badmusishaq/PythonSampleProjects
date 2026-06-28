import cv2, time, pandas
from datetime import datetime

first_frame = None  # Initialize the first frame variable
status_list = [None, None]  # Initialize a list to keep track of the status of motion detection
times = []  # Initialize a list to keep track of the times when motion is detected
df = pandas.DataFrame(columns=["Start", "End"])  # Create a DataFrame to store the start and end times of motion detection

video = cv2.VideoCapture(0)  # Open the default camera (0)

while True:
    check, frame = video.read()  # Read a frame from the camera

    status = 0  # Initialize the status variable
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # Apply Gaussian blur to the grayscale frame


    if first_frame is None:
        first_frame = gray_frame  # Set the first frame to the current grayscale frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)  # Compute the absolute difference between the first frame and the current frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]  # Apply a binary threshold to the delta frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the threshold frame

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:  # Ignore small contours
            continue
        status = 1  # Set the status to 1 if motion is detected

        (x, y, w, h) = cv2.boundingRect(contour)  # Get the bounding rectangle for the contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Draw a rectangle around the detected motion

    status_list.append(status)  # Append the status to the list

    if status_list[-1] == 1 and status_list[-2] == 0:  # If motion is detected
        times.append(datetime.now())  # Append the current time to the times list
        #print("Motion Detected!")  # Print a message to the console

    if status_list[-1] == 0 and status_list[-2] == 1:  # If motion has stopped
        times.append(datetime.now())  # Append the current time to the times list
        #print("Motion Stopped!")  # Print a message to the console

    #cv2.imshow("Capturing", frame)  # Display the captured frame in a window
    cv2.imshow("Gray Frame", gray_frame)  # Display the captured grayscale frame in a window
    cv2.imshow("Delta Frame", delta_frame)  # Display the delta frame in a window
    cv2.imshow("Threshold Frame", thresh_frame)  # Display the threshold frame in a window
    cv2.imshow("Color Frame", frame)  # Display the captured color frame in a window

    key = cv2.waitKey(1)  # Wait for a key press to close the window

    if key == ord('q'):  # If the 'q' key is pressed, exit the loop
        if status == 1:  # If motion is detected when exiting
            times.append(datetime.now())  # Append the current time to the times list
        break
print(status_list)  # Print the list of statuses to the console
print(times)  # Print the list of times to the console

for i in range(0, len(times), 2):  # Iterate through the times list in steps of 2
    #df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)  # Append the start and end times to the DataFrame
    df.loc[len(df)] = {"Start": times[i], "End": times[i + 1]}

df.to_csv("Times.csv")  # Save the DataFrame to a CSV file


video.release()  # Release the camera resource
cv2.destroyAllWindows()  # Close all windows