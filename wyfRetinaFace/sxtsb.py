# -*- coding: utf-8 -*-
import os

import face_recognition
import cv2

def sb():
    video_capture = cv2.VideoCapture(0)

    process_this_frame = True

    while True:
        images = os.listdir('image')
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            count = 0
            for face_encoding in face_encodings:
                for image in images:

                    # load the image

                    current_image = face_recognition.load_image_file("image/" + image)

                    # encode the loaded image into a feature vector

                    current_image_encoded = face_recognition.face_encodings(current_image)[0]

                    # match your image with the image and check if it matches

                    result = face_recognition.compare_faces(

                        [face_encoding], current_image_encoded)

                    # check if it was a match
                    count += 1

                    if result[0] == True:
                        print("Matched: " + image.split('.')[0])
                        name = image.split('.')[0]
                        break
                    if count == len(images):
                        print("无该人")
                        name = "无该人"

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()