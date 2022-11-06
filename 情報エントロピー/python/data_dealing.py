# coding=utf-8
import cv2
import numpy as np
from numba import jit
from PIL import Image
import os

dirname = "C:/Users/nowas/OneDrive - 同志社大学/ドキュメント/生産システム研究室/実験/22-04-26_deeplearning_生データonサーモ１/" #dir_path
dirname1 = dirname + "a_square/"

with os.scandir(dirname1) as folder:
        for entry in folder:
            if entry.is_dir():
                print("[folder] : ", entry.name)
                with os.scandir(dirname1 + entry.name) as file:
                    for ent in file:
                        print("--[file] : ", ent.name)
                        img1 = cv2.imread(dirname1+entry.name+"/"+ent.name, cv2.IMREAD_GRAYSCALE)
                            