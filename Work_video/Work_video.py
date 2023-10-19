import cv2
import sys
import numpy as np


# Загрузите видеофайл:
#from ffpyplayer.player import MediaPlayer
#video_path=("")
capture = cv2.VideoCapture(0)
#player = MediaPlayer(video_path)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Кадр - это изображение, которое вы хотите, флаг - это успех / неудача:
# face = cv2.MUL

# Перебирайте кадры видео:

while True:
    flag, frame = capture.read()
    #audio_frame, val = player.get_frame()

    if flag == 0:
        break

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("Video", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
        # Escape to exit
    if key_pressed == 27:
        break

capture.release()
cv2.destroyAllWindows()
