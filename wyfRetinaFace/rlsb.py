import os

import cv2
import face_recognition


def sb(path):
    images = os.listdir('images')
    face_names = []
    image_to_be_matched1 = face_recognition.load_image_file(path)
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched1)[0]


    name='unknow'
    for image in images:

            # load the image

        current_image = face_recognition.load_image_file("images/" + image)

            # encode the loaded image into a feature vector

        current_image_encoded = face_recognition.face_encodings(current_image)[0]

            # match your image with the image and check if it matches

        result = face_recognition.compare_faces(

                [image_to_be_matched_encoded], current_image_encoded)

            # check if it was a match

        if result[0] == True:
            print("Matched: " + image.split('.')[0])
            name = image.split('.')[0]

    return  name

