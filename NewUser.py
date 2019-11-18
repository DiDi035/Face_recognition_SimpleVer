import mysql.connector
import cv2
import numpy
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "face_recognition"
)

def insert_or_update(name):
    mycursor = mydb.cursor()
    mycursor.execute("select id from people_info where full_name = '" + str(name) + "';")
    result = mycursor.fetchall()
    check = 0
    for x in result:
        ID = x
        check = 1
        break
    if check == 1:
        print('The name '+ str(name) + ' has been used already !!')
        return 1, ID
    else:
        mycursor.execute("insert into people_info values('" + str(name) + "', NULL);")
        mydb.commit()
        mycursor.execute("select id from people_info where full_name = '" + str(name) + "';")
        list_id = mycursor.fetchall()
        for x in list_id:
            ID = x
    return 1, ID

name = input('Enter your fullname: ')
count = 0
shortName = ""
for x in name:
    if x != " ":
        shortName += x

exist, ID  = insert_or_update(name)
if exist != 0:
    print("ID for " + str(name) + ": " + str(ID))
    os.mkdir(shortName)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    video = cv2.VideoCapture(0)
    numOfPhoto = 0

    while video.isOpened():
        _, img = video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print(x, y, w, h)
            numOfPhoto = numOfPhoto + 1
            cv2.imwrite(shortName + "/" + str(ID) + "_" + str(numOfPhoto) + ".jpg", gray[y:y + h, x:x + w])
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif numOfPhoto > 200:
            break
    video.release()
    cv2.destroyAllWindows()
    print('Finish taking photo for ' + str(name))
    print('Add new user successfully !!')
