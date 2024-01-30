import cv2
import numpy as np

image = cv2.imread('players.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)


circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=10, maxRadius=50)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)


cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
