import cv2 

from random import randrange
#Taking in classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

#taking webcam feed 
webcam  = cv2.VideoCapture(0)

while True:
    successfull_frame_read,frame = webcam.read()

    #if there is not a successfull frame read 
    if not successfull_frame_read:
        break
    
    grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(grayscaled_frame)

    for (x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),4)

        the_face = frame[y:y+h,x:x+w]

        face_greyscaled=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
        
        smiles = smile_detector.detectMultiScale(the_face,scaleFactor=1.7,minNeighbors=20)

       # for (x_,y_,w_,h_) in smiles:
           # cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(randrange(256),randrange(256),randrange(256)),4)


        if len(smiles)>0:
            cv2.putText(frame,'Smiling',(x,y+h+40),fontScale=4,
            fontFace=cv2.FONT_HERSHEY_PLAIN,color=(randrange(256),randrange(256),randrange(256)))

    cv2.imshow('Smile detector Window',frame)


    key=cv2.waitKey(1)

    if key==81 or key==113:
        break 


webcam.release()
cv2.destroyAllWindows()



print('code completed')