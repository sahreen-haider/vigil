import os
import numpy as numpy
import cv2
from deepface import DeepFace 


class Detect_verify:
    def capture_live_faces(self):
        counter = 0
        model_names = ["opencv", "ssd", "dlib", "mtcnn"]
        # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame = cap.read()
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            # using "SSD(single shot detector)" for its faster performance
            # try:
            self.detected_face = DeepFace.extract_faces(self.frame, detector_backend = "ssd")
            faces = self.detected_face[0]["facial_area"]

            cv2.imshow("Detect Faces", self.frame)
            cv2.rectangle(self.frame, (faces["x"],faces["y"]), (faces["x"]+faces["w"], faces["y"]+faces["h"]), (255, 0, 0), 2)
            file_path = "/Volumes/Extended/projects/Vigil/dataset/recorded_data/recorded_sample"+str(counter)+".jpg"
            cv2.imwrite(file_path, self.frame)
            counter += 1
            #     break
            
            # except:
            #     continue

            


            if cv2.waitKey(1) & 0xFF == ord("v"):
                break


        cap.release() 
        cv2.destroyAllWindows()

        
obj = Detect_verify()
obj.capture_live_faces()


