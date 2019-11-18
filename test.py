import os
import numpy
rootPath = "/media/lisu/DATA/Face detection"
os.chdir(rootPath + "/" + "HuynhBaoDi")
listImage = os.listdir()
print(listImage)
os.chdir(rootPath)
print(os.listdir())

