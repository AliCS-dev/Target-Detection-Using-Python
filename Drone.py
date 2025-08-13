import argparse
import imutils #using it for basic image processsing
import cv2 

# argument parse
ap  = argparse.ArgumentParser()
ap.add_argument("-v","--video",help="path to the file")

args = vars(ap.parse_args())

#load the video
camera = cv2.VideoCapture(args["video"]) #Goal is to loop over each frame of the video

while True:
    #grab the current frame of the loop and make a status check if there is any target
    (grabbed, frame) = camera.read()
    status = "No Target Found!"

    #now check if all the frames have been checked
    if not grabbed:
        break

    #we can conver the frames in grey scale and blur it to detect the contours of objects
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(7,7),0)
    edged = cv2.Canny(blur,50,150)

    #finding edges
    contour = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contour = imutils.grab_contours(contour)


