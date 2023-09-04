import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\maddi\Desktop\codsoft\codsoft2\haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\maddi\Desktop\codsoft\codsoft2\IMG-20230904-WA0017.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4) 

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow('img',img)
cv2.waitKey()