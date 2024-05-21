# Virtual Painter 

## Description
#### This program is a simple drawing application using OpenCV and Mediapipe libraries in Python. Here's a breakdown of what it does:

##### Imports:It imports necessary libraries like OpenCV (cv2), NumPy (np), Mediapipe (mp), and deque from collections.<hr>

It detects hand landmarks using Mediapipe Hands.
It draws landmarks on the frame and detects the position of the index finger.
If the finger is below a certain threshold (indicating drawing mode), it adds the finger position to the appropriate color deque.
If the finger is in the color selection area, it changes the drawing color accordingly.
If the clear button is pressed, it resets all color deques and indices.

###### Colors:Purple,Green,Blue,Black,Yellow,pink, Aqua


It draws lines on the canvas and frame based on the points stored in the color deques.

It exits the program when the user presses 'q', releasing the webcam and destroyin.<hr>

![](https://github.com/ahmadmirdamadi/Virtual-Painter-/assets/113544813/19861f5f-9472-4906-8852-65a78fd56458)<hr>

Source:https://youtu.be/_aOS1ozt6ec?si=_bbhbBmMzHyECcAP
