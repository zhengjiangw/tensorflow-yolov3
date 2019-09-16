import cv2
import numpy as np


def check_annotation(img):
  
  content = {}
  with open("./data/dataset/people_train.txt", "r") as f:
    lines = f.readlines()
  
  for line in lines:
    splits = line.split(" ")
    img_name = splits[0]
    if img_name == img:
      for i in range(splits[1:] // 5):
        cv2.circle(img, (760, -114), 20, (255, 0, 0), 2)
        cv2.circle(img, (1026, 210), 20, (255, 0, 0), 2)
        
  img_path = "D:\dataset\detector\\train\\90004a8096d6237cf250b6de5ba07358.jpg"
  data = [760,-114,1026,210, 1118,92,1396,386]
  
  img = cv2.imread(img_path)
  
  cv2.circle(img, (1118, 92), 20, (255, 0, 0), 2)
  cv2.circle(img, (1396, 386), 20, (255, 0, 0), 2)
  cv2.imshow("test", img)
  cv2.waitKey(0)
  