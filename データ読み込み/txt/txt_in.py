import numpy as np
import os

#カレントディレクトリを現在のディレクトリに移動
#https://note.nkmk.me/python-script-file-path/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# テキストファイルのインプット
# https://tipstour.net/python-text-file-put-list
with open('filename.txt', 'r', encoding='UTF-8') as f:
    tmp = f.read().split("\n")
f.close()

# print(tmp)

num = []
for i in range(len(tmp)):
    if tmp[i] != '':
        #自分で型を指定する
        num.append(float(tmp[i]))

# 一次元配列を二次元配列にする
ret = np.array(num).reshape(-1,62)

print(ret)

