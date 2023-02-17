import cv2

cap = cv2.VideoCapture(0)

orejaClassif = cv2.CascadeClassifier('cascade.xml')

while True:
	
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	ear = orejaClassif.detectMultiScale(gray,
	scaleFactor = 5,
	minNeighbors = 91,
	minSize=(70, 78))

	for (x,y,w,h) in ear:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame,'oreja',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

	cv2.imshow('Siguiendo',frame)
	
	if cv2.waitKey(1) == 25:
		break
cap.release()
cv2.destroyAllWindows()
