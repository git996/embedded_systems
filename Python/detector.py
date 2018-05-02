import cv2
import logging as log
from time import sleep
import serial 
import sys
# import winsound
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
        ser = serial.Serial('COM4', 9600)
        
        #for ubuntu
        #ser = serial.Serial('/dev/ttyACM0', 9600)

        frame_dimesion = [640, 480]
        servo_max = 150
        base_servo = 90
        # face_limit = []




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
            #condinitonal statement below if executed if only 1 face is detected.
            if (len(faces) == 1):
                for (x, y, w, h) in faces:
                    #default shows screen size is 480(H) X 640(W).
                    a = int(x + (w/2))
                    b = int(y + (h/2))
                    #draw a TINY rectangle at the centre of the face so it look like a dot.
                    x = cv2.rectangle(frame, (a, b), (a, b), (120, 120, 0), 3)
                    center = cv2.rectangle(frame, (320,240), (320,240), (500, 500, 0), 3)
                    # frame_center = [350, 240]
                    
                    face_center = [a,b]

                    for coordinates in face_center:
                        sleep(.015)
                        x_coord = face_center[0]
                        y_coord =  frame_dimesion[1] - face_center[1] 
                        print('Face: ', x_coord, ',  ', y_coord)
                        mapped_x = int(176 - (x_coord / (frame_dimesion[0]/servo_max)))
                        mapped_y = int(180 - (y_coord / (frame_dimesion[1]/servo_max)))

                        # if mapped_x > 50:
                        #     mapped_x = mapped_x - 20
                        # elif x_coord < 40:
                        #     mapped_x = mapped_x + 20

                        # move the base servo (in the x axis) if object gets close to the edge
                        if mapped_x > 130 and  base_servo < 160:
                            base_servo = base_servo + 20;

                        if mapped_x < 30 and base_servo > 20:
                            base_servo = base_servo - 20;

                        val = 'X' + str(mapped_x) + 'Y' + str(mapped_y) +'Z'+str(int(base_servo))
                        val = val.encode('utf-8')
                        print('Serial Val: ',val)
                        ser.write(val)

            # Display the resulting frame
            #if multiple faces are detected. don't send serail data to the servos
            elif (len(faces) < 1):
                pass
            else:
                print('Multiple Faces Detected!')
                # winsound.Beep(500, 500)
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

