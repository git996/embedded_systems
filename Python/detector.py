import cv2
import logging as log
from time import sleep
import serial 
import sys
def main():
    print('hi')

    # ser = serial.Serial('COM3', 9600)
    

    #instantiate the class
    d  = Detector()
    d.detect()


class Detector:

    def detect(self):

        #the haar cascade for fontl face model
        cascPath = "./haarcascades/haarcascade_frontalface_default.xml"

        #set the camera port
        camera_port = 0
        #set frames
        ramp_frames = 30

        #pass to the loaded cascaded to cv2
        classifier = cv2.CascadeClassifier(cascPath)

        #set viedo capture
        video_capture = cv2.VideoCapture(camera_port)
        #create a log file for the webcam
        log.basicConfig(filename='webcam.log',level=log.INFO)
        anterior = 0

        #initserial
        #ser = serial.Serial('COM1', 9600)
        
        #for ubuntu
        ser = serial.Serial('COM2', 9600)




        while True:
            # sleep(1)
            if not video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass

            # Capture frame-by-frame
            ret, frame = video_capture.read()

            #convert each frame to gray
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = classifier.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
              #Draw a rectangle around the faces
            
            # Font= cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, hscale= FontSize, vscale= 1.0, shear=0, thickness=1, lineType=8)
            if len(faces) > 0:
                val = "t1"
                val = val.encode('utf-8')
                ser.write(val)
                for (x, y, w, h) in faces:
                    #default shows screen size is 480(H) X 640(W).
                    a = int(x + (w/2))
                    b = int(y + (h/2))
                    #draw a TINY rectangle at the centre of the face so it look like a dot.
                    x = cv2.rectangle(frame, (a, b), (a, b), (500, 500, 0), 3)
                    center = cv2.rectangle(frame, (320,240), (320,240), (500, 500, 0), 3)
                    frame_center = [320, 240]
                    face_center = [a,b]
                    
                    # for refrence, face in zip(frame_center, face_center):
                        
                    #     if(abs(refrence - face) > 10):
                    #         print('Needs to move')
                    #     else:
                    #        print('No Need to move') 

                    # print('Frame Center: ', frame_center)
                    # print('Face Center: ', face_center)
            # Display the resulting frame
            
            else:
                val = 't0'
                val = val.encode('utf-8')
                ser.write(val)
                pass
            cv2.imshow('Detections', frame)
            #add a event listener to close the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                sys.exit()
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

