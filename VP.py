import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# Initialize color index and points deque for different colors
colorIndex = 0
bpoints = [deque(maxlen=512)]
gpoints = [deque(maxlen=512)]
rpoints = [deque(maxlen=512)]
kpoints = [deque(maxlen=512)]
ypoints = [deque(maxlen=512)]
ppoints = [deque(maxlen=512)]
apoints = [deque(maxlen=512)]

blue_index = 0
green_index = 0
red_index = 0
black_index = 0
yellow_index = 0
pink_index = 0
aqua_index = 0

colors = [(128, 0, 128), (0, 128, 0), (128, 0, 0), (0, 0, 0), (0, 255, 255), (255, 192, 203), (255, 255, 0)]

# Function to draw a square with a white border
def draw_square_with_white_border(image, center, size, color, border_thickness):
    x, y = center
    half_size = size // 2
    cv2.rectangle(image, (x - half_size, y - half_size), (x + half_size, y + half_size), color, -1)
    border_color = (255, 255, 255)
    cv2.rectangle(image, (x - half_size - border_thickness, y - half_size - border_thickness),
                  (x + half_size + border_thickness, y + half_size + border_thickness), border_color, border_thickness)

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)
ret = True
while ret:
    # Read each frame from the webcam
    ret, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Canvas setup
    paintWindow = np.zeros((x, y, 3)) + 0
    paintWindow = cv2.rectangle(paintWindow, (30, 10), (110, 90), (255, 255, 255), -1)
    paintWindow = cv2.rectangle(paintWindow, (220, 10), (300, 90), (128, 0, 128), -1)
    paintWindow = cv2.rectangle(paintWindow, (420, 10), (500, 90), (0, 128, 0), -1)
    paintWindow = cv2.rectangle(paintWindow, (620, 10), (700, 90), (128, 0, 0), -1)
    paintWindow = cv2.rectangle(paintWindow, (820, 10), (900, 90), (0, 0, 0), -1)
    paintWindow = cv2.rectangle(paintWindow, (820, 150), (900, 230), (0, 255, 255), -1)
    paintWindow = cv2.rectangle(paintWindow, (820, 300), (900, 380), (255, 192, 203), -1)
    paintWindow = cv2.rectangle(paintWindow, (820, 450), (900, 530), (255, 255, 0), -1)

    draw_square_with_white_border(paintWindow, (70, 50), 80, (255, 255, 255), 3)
    draw_square_with_white_border(paintWindow, (260, 50), 80, (128, 0, 128), 3)
    draw_square_with_white_border(paintWindow, (460, 50), 80, (0, 128, 0), 3)
    draw_square_with_white_border(paintWindow, (660, 50), 80, (128, 0, 0), 3)
    draw_square_with_white_border(paintWindow, (860, 50), 80, (0, 0, 0), 3)
    draw_square_with_white_border(paintWindow, (860, 190), 80, (0, 255, 255), 3)
    draw_square_with_white_border(paintWindow, (860, 340), 80, (255, 192, 203), 3)
    draw_square_with_white_border(paintWindow, (860, 490), 80, (255, 255, 0), 3)

    cv2.putText(paintWindow, "CLEAR", (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "PURPLE", (233, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "GREEN", (435, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "BLUE", (637, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "BLACK", (835, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "YELLOW", (830, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "PINK", (840, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "AQUA", (840, 495), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

    frame = cv2.rectangle(frame, (30, 10), (110, 90), (255, 255, 255), -1)
    frame = cv2.rectangle(frame, (220, 10), (300, 90), (128, 0, 128), -1)
    frame = cv2.rectangle(frame, (420, 10), (500, 90), (0, 128, 0), -1)
    frame = cv2.rectangle(frame, (620, 10), (700, 90), (128, 0, 0), -1)
    frame = cv2.rectangle(frame, (820, 10), (900, 90), (0, 0, 0), -1)
    frame = cv2.rectangle(frame, (820, 150), (900, 230), (0, 255, 255), -1)
    frame = cv2.rectangle(frame, (820, 300), (900, 380), (255, 192, 203), -1)
    frame = cv2.rectangle(frame, (820, 450), (900, 530), (255, 255, 0), -1)

    draw_square_with_white_border(frame, (70, 50), 80, (255, 255, 255), 3)
    draw_square_with_white_border(frame, (260, 50), 80, (128, 0, 128), 3)
    draw_square_with_white_border(frame, (460, 50), 80, (0, 128, 0), 3)
    draw_square_with_white_border(frame, (660, 50), 80, (128, 0, 0), 3)
    draw_square_with_white_border(frame, (860, 50), 80, (0, 0, 0), 3)
    draw_square_with_white_border(frame, (860, 190), 80, (0, 255, 255), 3)
    draw_square_with_white_border(frame, (860, 340), 80, (255, 192, 203), 3)
    draw_square_with_white_border(frame, (860, 490), 80, (255, 255, 0), 3)

    cv2.putText(frame, "CLEAR", (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "PURPLE", (233, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (435, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (637, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLACK", (835, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (830, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "PINK", (840, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "AQUA", (840, 495), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # Post-process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * y)
                lmy = int(lm.y * x)
                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0], landmarks[8][1])
        center = fore_finger
        cv2.circle(frame, center, 3, (0, 255, 0), -1)

        # If the user is drawing
        if center[1] > 100:
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                kpoints[black_index].appendleft(center)
            elif colorIndex == 4:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 5:
                ppoints[pink_index].appendleft(center)
            elif colorIndex == 6:
                apoints[aqua_index].appendleft(center)
        else:
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            kpoints.append(deque(maxlen=512))
            black_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1
            ppoints.append(deque(maxlen=512))
            pink_index += 1
            apoints.append(deque(maxlen=512))
            aqua_index += 1

        # Check if the user is selecting a color
        if center[1] <= 90:
            if 30 <= center[0] <= 110:  # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                kpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                ppoints = [deque(maxlen=512)]
                apoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                black_index = 0
                yellow_index = 0
                pink_index = 0
                aqua_index = 0

                paintWindow[100:, :, :] = 0
            elif 220 <= center[0] <= 300:
                colorIndex = 0  # Purple
            elif 420 <= center[0] <= 500:
                colorIndex = 1  # Green
            elif 620 <= center[0] <= 700:
                colorIndex = 2  # Red
            elif 820 <= center[0] <= 900:
                colorIndex = 3  # Black
        elif 150 <= center[1] <= 230:
            if 820 <= center[0] <= 900:
                colorIndex = 4  # Yellow
        elif 300 <= center[1] <= 380:
            if 820 <= center[0] <= 900:
                colorIndex = 5  # Pink
        elif 450 <= center[1] <= 530:
            if 820 <= center[0] <= 900:
                colorIndex = 6  # Aqua
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        kpoints.append(deque(maxlen=512))
        black_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1
        ppoints.append(deque(maxlen=512))
        pink_index += 1
        apoints.append(deque(maxlen=512))
        aqua_index += 1

    # Draw lines of all the colors on the canvas and frame
    points = [bpoints, gpoints, rpoints, kpoints, ypoints, ppoints, apoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Output", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
