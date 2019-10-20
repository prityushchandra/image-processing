#!/usr/bin/env python
import numpy as np
import cv2


def nothing(x):
	pass

def get_frame(cap, scaling_factor):
    # Capture the frame from video capture object
    ret, frame = cap.read()

    # Resize the input frame
    frame = cv2.resize(frame, None, fx=scaling_factor,
            fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5


def greenCircleDetect():
	#ret, frame = cap.read()
	#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([36, 0, 0])
	upper_blue = np.array([86, 255, 255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(frame, contours, -1, (255, 255, 0))
	#cv2.imshow('frame', frame)
	#cv2.imshow('green_output', mask)


def blueCircleDetect():
	#ret, frame = cap.read()
	#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([62, 146, 51])
	upper_blue = np.array([179, 255, 100])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(frame, contours, -1, (0, 255, 0))
	#cv2.imshow('frame', frame)
	#cv2.imshow('blue_output', mask)



def redCircleDetect():
	#ret, frame = cap.read()
	#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([0, 166, 52])
	upper_blue = np.array([179, 255, 255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(frame, contours, -1, (0, 255, 0))

	#cv2.imshow('frame', frame)
	#cv2.imshow('red_output', mask)

while True:

	frame = get_frame(cap, scaling_factor)##scaling factor is defined as size of window you want
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	greenCircleDetect()

	redCircleDetect()

	blueCircleDetect()

	cv2.imshow('frame', frame)



	key=cv2.waitKey(1)
	if key==27:
		break



cap.release()
cv2.destroyAllWindows()
