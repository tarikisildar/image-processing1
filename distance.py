import numpy as np
import cv2

def find_marker(image): #this function finds and returns the contour which covers max area
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5, 5), 0)
    edged = cv2.Canny(gray, 35,125)

    (img,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts,key = cv2.contourArea)

    return cv2.minAreaRect(c)

def distance_to_camera(knownwidth, focallength, perwidth): #Used pythagorean theorem
    return (knownwidth * focallength) / perwidth

KNOWNDISTANCE = 32.0
KNOWNWIDTH = 21.0
IMAGEPATHS = ['a30.jpg','at50.jpg','a80.jpg']

image = cv2.imread(IMAGEPATHS[0])
marker = find_marker(image)
focallength = (marker[1][0] * KNOWNDISTANCE )/ KNOWNWIDTH

for at in IMAGEPATHS:
    image = cv2.imread(at)
    marker = find_marker(image)
    inches = distance_to_camera(KNOWNWIDTH,focallength,marker[1][0])
    print(inches)

    box = np.int0(cv2.boxPoints(marker))
    cv2.drawContours(image,[box],-1, (0,255,0),2)
    cv2.putText(image, "%.1fcm" % inches,(30,70), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
    cv2.imshow("asd.jpg", image)
    cv2.waitKey(0)
