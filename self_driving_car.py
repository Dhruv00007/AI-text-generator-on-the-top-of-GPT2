import cv2
from random import randrange 

video = cv2.VideoCapture('pedestrian.mp4')

# loading car pre trained data 
car_tracker_file = 'cars.xml'
car_tracker = cv2.CascadeClassifier(car_tracker_file)
# loading prdestrian pre trained data 
pedestrian_tracker_file = 'haarcascade_fullbody.xml'
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)



while True:
    (read_successful,frame) =  video.read()

    if read_successful:
        #converting image into grayscale 
        grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break



    # detecting cars and pedestrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    
    
    #drawing rectangles around 
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),4) 

    #drawing rectangles around pedestrian
    for (x,y,w,h) in pedestrians:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),4) 


    #showing cars 
    cv2.imshow('desktop window',frame)



    key = cv2.waitKey(1)

    if key==81 or key==113:
        break


video.release()


print('code completed')
# #reading the test image 
# car image to test the data 
#image_file = 'car highway.jpg'
# image = cv2.imread(image_file)


# #taking pre trained data 
# 

# #converting image into black and white 
# grayscaled_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# #tracking cars 
# cars = car_tracker.detectMultiScale(grayscaled_img)


# # drawing rectangles over detected cars 
# for (x,y,w,h) in cars:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)

# #displaying the image 
# cv2.imshow('desktop window',image)
