import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
import os

#カレントディレクトリを現在のディレクトリに移動
#https://note.nkmk.me/python-script-file-path/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(10):
    x = np.arange(30)
    y = randint(0, 100, 30)
    plt.plot(x, y, color = "k", marker = "o", label = "Array elements")

    dirname = "soma"
    os.makedirs(dirname, exist_ok = True)
    #pngで保存（sekiokaフォルダ）
    plt.savefig("./" + dirname + "/" + str(i) + ".png")

    # 大量のデータだとout of memoryが発生するから下のようにする(無くても動いた)ないときはplt.figure()にした
    #https://qiita.com/Masahiro_T/items/bdd0482a8efd84cdd270
    plt.close()
    plt.clf()

