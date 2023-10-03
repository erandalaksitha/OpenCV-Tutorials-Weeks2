#Python | Program to extract frames using OpenCV

import cv2

def FrameCapture(path):

	vidObj = cv2.VideoCapture(path)

	count = 0

	success = 1

	while success:

		success, image = vidObj.read()

		cv2.imwrite("capture%d.jpg" % count, image)

		count += 1



if __name__ == '__main__':

	FrameCapture("C:\\Users\\ERANDA WITHANAGE\\Downloads\\pexels_videos_1249406 (1080p).mp4")
