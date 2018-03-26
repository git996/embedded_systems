import cv2
import logging as log
from time import sleep
import sys
def main():
    print('hi')

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



        while True:
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
            for (x, y, w, h) in faces:
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (120, 2, 0), 2)
                a = int(x + (w/2))
                b = int(y + (h/2))
                # eye = [int(a-(a/2)), int(b-(b/2))]
                #draw a TINY rectangle at the centre of the face so it look like a dot.
                x = cv2.rectangle(frame, (a, b), (a, b), (500, 500, 0), 3)
                print(a,',',b)

            if len(faces) > 0:
                # print(frame)
                print('SHape', frame.shape)

            # Display the resulting frame
            cv2.imshow('Detections', frame)
            
            #add a event listener to close the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                sys.exit()


        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

