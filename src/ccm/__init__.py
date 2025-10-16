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
    if(len(faces)==0):
        print('NOOOOOOO')
    else:
        print(str(len(faces)) + 'YAAAAY')
    return faces

def draw_bounding_box(frame, detected_objects):
    for (x,y,w,h) in detected_objects:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)


# @TODO   
def max_bb(l1, l2):
    if(l1==[]):
        return l2
    if(l2==[]):
        return l1
    l=[]
    for(x1,y1,w1,h1) in l1:
        for (x2, y2, w2, h2) in l2:
            x = x1 if x1<x2 else x2
            y = y1 if y1<y2 else y2
            w = w1 if w1>w2 else w2
            h = h1 if h1>h2 else h2
            l+=[x,y,w,h]
    return l

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    draw = []
    detected_objects = detect_bounding_box(frame)
    draw_bounding_box(frame, detected_objects)
    #draw += max_bb(draw, detected_objects)
    
    # Find Canny edges 
    edged = cv.Canny(frame, 30, 200) 
    
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image 
    copy = gray.copy() 
    contours, hierarchy = cv.findContours(copy, 
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
    
    # Draw all contours 
    # -1 signifies drawing all contours 
    cv.drawContours(copy, contours, -1, (0, 255, 0), 3) 
    
    # Display the resulting frame
    cv.imshow('Cam Capture Manipulation', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
