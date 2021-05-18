import cv2 
from random import randrange 


# loading pre trained data from already downloaded files 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#selecting an image 
#img = cv2.imread('detection.png')
webcam = cv2.VideoCapture(0)


while True:
    successful_frame_read,frame = webcam.read()

    #converting image to gray 
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #drawing a rectangle 
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
    
    #showing the image 
    cv2.imshow('dekstop window',frame)
 
    key=cv2.waitKey(1)
    #press Q to quit
    if key==81 or key==113:
        break 

# release the webcam
webcam.release()



"""
print(face_coordinates)
#for window to be open untill until one clicks a button 
cv2.waitKey()

print("code completed")

"""

print("code completed")