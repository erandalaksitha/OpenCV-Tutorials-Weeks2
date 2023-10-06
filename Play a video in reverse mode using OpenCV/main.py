import cv2 

cap = cv2.VideoCapture("C:\\Users\\ERANDA WITHANAGE\\Downloads\\pexels_videos_1249406 (1080p).mp4") 

check , vid = cap.read() 

counter = 0
check = True
frame_list = [] 

while(check == True): 

	cv2.imwrite("frame%d.jpg" %counter , vid) 
	check , vid = cap.read() 
	frame_list.append(vid) 
	
	counter += 1

frame_list.pop() 

for frame in frame_list: 
	
	cv2.imshow("Frm" , frame) 
	
	if cv2.waitKey(25) and 0xFF == ord("q"): 
		break
	
cap.release() 

cv2.destroyAllWindows() 

frame_list.reverse() 

for frame in frame_list: 
	cv2.imshow("Frame" , frame) 
	if cv2.waitKey(25) and 0xFF == ord("q"): 
		break

cap.release() 
cv2.destroyAllWindows() 
