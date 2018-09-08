import cv2
import numpy as np
from goprocam import GoProCamera
from goprocam import constants
import urllib.request
import threading
import traceback
averages = []

#List of possible classifiers from OpenCV Classifier human body recognition
classfiers = [
   "haarcascade_eye_tree_eyeglasses.xml" , #0
   "haarcascade_eye.xml" , #1
   "haarcascade_frontalcatface_extended.xml" , #2
   "haarcascade_frontalcatface.xml" , #3
   "haarcascade_frontalface_alt_tree.xml" , #4
   "haarcascade_frontalface_alt.xml" , #5
   "haarcascade_frontalface_alt2.xml" , #6
   "haarcascade_frontalface_default.xml" , #7
   "haarcascade_fullbody.xml" , #8
   "haarcascade_lefteye_2splits.xml" , #9
   "haarcascade_licence_plate_rus_16stages.xml" , #10
   "haarcascade_lowerbody.xml" , #11
   "haarcascade_profileface.xml" , #12
   "haarcascade_righteye_2splits.xml" , #13
   "haarcascade_russian_plate_number.xml" , #14
   "haarcascade_smile.xml" , #15
   "haarcascade_upperbody.xml" #16
]

#Assign classifier
chosenClassifier = classfiers[8]

#cascPath varies based on local machine.  /usr/local/share/ is the main difference amongst machines
cascPath="/anaconda3/lib/python3.6/site-packages/cv2/data/" + chosenClassifier  #Raghav's path
#cascPath="/usr/local/share/opencv/haarcascades/" + chosenClassifier            #The rest

#Path to classifier
bodyCascade = cv2.CascadeClassifier(cascPath)

#Setting GoPro parameters
gpCam = GoProCamera.GoPro()
gpCam.gpControlSet(constants.Stream.BIT_RATE, constants.Stream.BitRate.B2_4Mbps)
#gpCam.gpControlSet(constants.Stream.WINDOW_SIZE, constants.Stream.WindowSize.W480)

#Read media buffer from udp port 10000
cap = cv2.VideoCapture("udp://127.0.0.1:10000")


def stream_on(i):
    count = 0
    while True:

        ret, frame = cap.read()         # Capture frame-by-frame from GoPro

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Classifier attributes
        bodies = bodyCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        count += 1
        #Draw a rectangle around the bodies
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("GoPro OpenCV", frame)         # Display the resulting frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()               # \ Get rid of allocated resources
    cv2.destroyAllWindows()     # /

t = threading.Thread(target = stream_on, args=(1,))
t.start()
