import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
import os

#カレントディレクトリを現在のディレクトリに移動
#https://note.nkmk.me/python-script-file-path/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = np.arange(30)
y = randint(0, 100, 30)
plt.plot(x, y, color = "k", marker = "o", label = "Array elements")

dirname = "soma"
os.makedirs(dirname, exist_ok = True)
#pngで保存（sekiokaフォルダ）
plt.savefig(".\\" + dirname + "\\" + str(dirname) + ".png")
