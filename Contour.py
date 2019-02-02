import cv2

import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame2 = cv2.flip(frame, 1)

    blurred_frame = cv2.GaussianBlur(frame2, (5, 5), 0)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame2, contours, -1,  (0, 255, 0), 3)

    cv2.imshow("frame2", frame2)
    cv2.imshow("BLue", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()