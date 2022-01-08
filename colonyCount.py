#
# colonyCount.py : Identify and count E. coli colonies in a petri dish
#

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# Read input image
image = cv2.imread(args["image"])

def ManualThresholdFluorescentGreen(inputImage):
    blue = 151
    green = 200
    red = 42
    halfWin = 35

    lower_color_bounds = np.array([blue-halfWin, green-halfWin, red-halfWin])
    upper_color_bounds = np.array([blue+halfWin, green+halfWin, red+halfWin])

    newImg = cv2.inRange(image, lower_color_bounds, upper_color_bounds)
    imgGray = cv2.cvtColor(newImg, cv2.COLOR_GRAY2BGR)
    (T, imgBinary) = cv2.threshold(imgGray, 200, 255, cv2.THRESH_BINARY)
    return imgBinary

imgBinary = ManualThresholdFluorescentGreen(image)

cv2.imwrite("C:/project/ecoliBinary.JPG", imgBinary)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(T, threshInv) = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY_INV |
                               cv2.THRESH_OTSU)

f, axs = plt.subplots(1,3,figsize=(12,5))
axs[0].imshow(image)
#axs[1].imshow(imgBinary)
axs[1].imshow(gray)
axs[2].imshow(threshInv)

plt.show()

