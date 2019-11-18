import cv2
import numpy
from PIL import Image
import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database = "face_recognition"
 )

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
recognizer.read('recognizer/trainner.yml')

def getInfoById(id):
    mycursor = mydb.cursor()
    mycursor.execute("select full_name from people_info where id = " + str(id) + ";")
    listFullName = mycursor.fetchall()
    for x in listFullName:
        name = str(x)
    print(name)

video = cv2.VideoCapture(0)
while video.isOpened():
    _, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        ID, dist = recognizer.predict(gray[y:y+h,x:x+w])
        print("Distance: " + str(dist))
        if (dist <= 40):
            getInfoById(ID)
        else:
            print('Unknown')
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
