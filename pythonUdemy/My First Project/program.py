import time 
import os
import pandas
import cv2


while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st2"])
    else:
        print("File not found")
    time.sleep(10)