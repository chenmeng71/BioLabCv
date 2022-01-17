#
# colonyCount.py : Identify and count E. coli colonies in a petri dish
#

import cv2
import imutils
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
ap.add_argument("-a", "--algorithm", type=str, required=False,
	help="detection algorithm, \"otsu\" or \"manual\"")
args = vars(ap.parse_args())

# Read input image
image = cv2.imread(args["image"])
useManual = args["algorithm"] == "manual"

def ManualThresholdFluorescentGreen(inputImage):
    blue = 151
    green = 200
    red = 42
    halfWin = 35

    lower_color_bounds = np.array([blue-halfWin, green-halfWin, red-halfWin])
    upper_color_bounds = np.array([blue+halfWin, green+halfWin, red+halfWin])

    newImg = cv2.inRange(inputImage, lower_color_bounds, upper_color_bounds)
    imgGray = cv2.cvtColor(newImg, cv2.COLOR_GRAY2BGR)
    (T, imgBinary) = cv2.threshold(imgGray, 200, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(imgBinary, cv2.COLOR_BGR2GRAY)

def OtsuThreshold(inputImage):
    imgGray = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
    (T, threshImg) = cv2.threshold(imgGray, 0, 255,
                               cv2.THRESH_OTSU)
    return threshImg

def DistanceTransform(inputImage):
    dist_transform = cv2.distanceTransform(inputImage, cv2.DIST_L2, 5)
    ret, last_image =  cv2.threshold(dist_transform, 0.3*dist_transform.max(),255,0)
    return np.uint8(last_image)

def Display(count, image1, image2, image3):
    f, axs = plt.subplots(1,3,figsize=(12,5))
    axs[0].set_title("Counted Colonies: {}".format(count))
    axs[1].set_title("Object Detection")
    axs[2].set_title("Distance Transform")
    axs[0].imshow(image1)
    axs[1].imshow(image2)
    axs[2].imshow(image3)
    plt.show()

def OtsuTransform(inputImg):
    otsuImg = OtsuThreshold(inputImg)
    return DistanceTransform(otsuImg)

def ManualTransfor(inputImg):
    manualImg = ManualThresholdFluorescentGreen(inputImg)
    return DistanceTransform(manualImg)

recognitionImg = OtsuThreshold(image)
distanceImg = OtsuTransform(image)

if useManual:
    recognitionImg = ManualThresholdFluorescentGreen(image)
    distanceImg = ManualTransfor(image)

cnts = cv2.findContours(distanceImg.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)

print("Count: %d" % (len(cnts)))

for (i, c) in enumerate(cnts):
	cv2.drawContours(image, [c], -1, (255, 0, 0), 2)
	
Display(len(cnts), image,
        recognitionImg,
        distanceImg)
