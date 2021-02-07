'''
pip install opencv-python
pip install numpy
pip install matplotlib
'''

# Python code to read image
import cv2

img = cv2.imread("google.png", cv2.IMREAD_COLOR)

cv2.imshow("Hello ", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
