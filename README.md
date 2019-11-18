Simple face recognition using python, opencv and "Haar Cascade classifier"
- "NewUser.py" will ask you to input your fullname, then automatically capture some pictures of your face on front camera. The pictures will be stored in a folder with your fullname in it and your information is stored in MySQL database table.
- "Train.py" will train the recognizer by pictures and information from database, then save the recognizer in folder "recognizer"
- "FaceRecognizer.py" will detect your face on camera and use the "recognizer" to recognize and output your fullname on terminal. 
- Because the purpose of building this was just learning how to use Python, so i used a really old and easy algorithms of face detection and recognization, therefor, the accuracy is just about 65-70% :(

 
