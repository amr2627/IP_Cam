# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:05:14 2020

@author: amar
"""

import urllib.request
import cv2
import numpy as np

url='http://192.168.43.141:8080/shot.jpg'

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    img=cv2.imdecode(imgNp,cv2.IMREAD_COLOR)
    
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)