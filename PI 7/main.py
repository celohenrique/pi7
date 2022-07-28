import torch
import pandas as pd
import cv2
import numpy as np
# Model
def class_detect():
    #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
    model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')


    cap = cv2.VideoCapture(0)
    while (1):
        sucess, img = cap.read()
        label = ''

        # img = cv2.imread('images/metal14.jpg') # or file, Path, PIL, OpenCV, numpy, list
        # Inference
        results = model(img)
        a = (results.pandas().xyxy[0])
        array = a[['name']].to_numpy()
        object = a.iloc[:, -1].values
        if not array.any():
            print('Nothing')
        cv2.imshow('Image', img)
        k = cv2.waitKey(1)
        if array.any():
            results.show()
            break

class_detect()