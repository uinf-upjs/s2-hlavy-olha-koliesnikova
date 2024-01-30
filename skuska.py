import cv2
import numpy as np

image = cv2.imread("team.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=70,
                           param1=200, param2=40, minRadius=30, maxRadius=80)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        if y < 200:
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)

cv2.imshow("Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
