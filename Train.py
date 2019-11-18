import os
import cv2
import numpy
import mysql.connector
from PIL import Image

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database = "face_recognition"
 )
mycursor = mydb.cursor()
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
idTrainData = []
imageTrainData = []
rootPath = "/media/lisu/DATA/Face detection"
mycursor.execute("select full_name from people_info;")
listFullName = mycursor.fetchall()
for n in listFullName:
    tmp = str(n)
    name = ""
    for x in tmp:
        if x != "," and x != "'" and x != "(" and x != ")":
            name+=x
    shortName = ""                                                              
    for x in name:                                                              
        if x != " " and x != "," and x != "'" and x != "(" and x != ")":
            shortName += x
    os.chdir(rootPath + "/" + str(shortName))
    mycursor.execute("select id from people_info where full_name = '" + str(name) + "';")
    listId = mycursor.fetchall()
    for y in listId:
        ID = y
    listImage = os.listdir()
    for i in listImage:
        img = str(i)
        print(img)
        plilImage = Image.open(img).convert('L')
        imageNp = numpy.array(plilImage)
        detectFaceInImage = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in detectFaceInImage:
            imageTrainData.append(imageNp[y:y+h, x:x+w])
            idTrainData.append(ID)
    os.chdir(rootPath)
recognizer.train(imageTrainData, numpy.array(idTrainData))
recognizer.save('recognizer/trainner.yml')

print("TRAINED SUCCESSFULLY !!!!!!!!!!!!!!!!!!!!!")

        

