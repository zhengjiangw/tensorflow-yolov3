import os

import cv2
import numpy as np


def check_annotation(name):
  
  content = {}
  with open("./data/dataset/people_train.txt", "r") as f:
    lines = f.readlines()
  
  for line in lines:
    splits = line.split(" ", maxsplit=1)
    img_name = splits[0]
    if img_name == name:
      
      coors = line.split(" ", maxsplit=1)[1][:-1].split(" ")
      coors = [c.split(",") for c in coors]
      break
  
  base_path = "D:\dataset\detector\\train"
  img = cv2.imread(os.path.join(base_path, name))
  h, w, _ = img.shape
  
  coors = np.array(coors).reshape(-1, 5)[:, 0:4].reshape(-1, 2, 2).astype(np.int)
  coors[:, :, 0] = np.clip(coors[:, :, 0], 0, w - 1)
  coors[:, :, 1] = np.clip(coors[:, :, 1], 0, h - 1)
  
  for coor in coors:
    
    cv2.rectangle(img, (coor[0][0], coor[0][1]), (coor[1][0], coor[1][1]), (255, 0, 0), 2)
    
  cv2.imshow("test", img)
  cv2.waitKey(0)


check_annotation("61a4091324d1983534ca23b6f007f841.jpg")
