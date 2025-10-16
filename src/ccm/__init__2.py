'''
C C M
======================
CamCaptureManipulation
======================
'''
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(vid):
    gray_image = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = detect_bounding_box(frame)
    
    # detect face
    face = face_classifier.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=20, minSize=(40, 40)
    )
    
    # draw bounding box
    for (x, y, w, h) in face:
        cv.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 4)
    
    # Find Canny edges 
    edged = cv.Canny(frame, 30, 200) 
    
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image 
    copy = frame.copy() 
    contours, hierarchy = cv.findContours(copy, 
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
    
    print('Found ' + str(len(contours)) + ' contours.')
    
    # Draw all contours 
    # -1 signifies drawing all contours 
    cv.drawContours(copy, contours, -1, (0, 255, 0), 3) 
    
    cv.imshow('Contours', copy) 

    
    
    # Display the resulting frame
    cv.imshow('Cam Capture Manipulation', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
