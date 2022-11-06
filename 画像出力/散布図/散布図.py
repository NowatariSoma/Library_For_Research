# visualize evaluation
import matplotlib.pylab as plt
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("img", exist_ok = True)

#論文用
#https://qiita.com/qsnsr123/items/325d21621cfe9e553c17
plt.rcParams['font.family'] ='sans-serif'#使用するフォント
plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
plt.rcParams['font.size'] = 15 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ

# #input
input_csv = pd.read_csv('log.csv')

#csvの列ごとにデータを拝借
fi_column_data = input_csv[input_csv.keys()[0]]
se_column_data = input_csv[input_csv.keys()[1]]
th_column_data = input_csv[input_csv.keys()[2]]
fo_column_data = input_csv[input_csv.keys()[3]]
fiv_column_data = input_csv[input_csv.keys()[4]]

plt.figure()
#x軸, y軸にラベル付け
plt.xlabel("epoch")
plt.ylabel(input_csv.keys()[1])
#プロットした　進捗用なので色は白黒になるようにした　グレー変換でもいいかも
plt.scatter(fi_column_data, se_column_data, linestyle='solid', facecolor = 'k', marker = 'x', s = 15, label = "training data")
plt.scatter(fi_column_data, fo_column_data, facecolor='None', edgecolors='k', s = 15, label = "validation data")
plt.legend()
plt.savefig("./img/1.png")
# plt.show()

plt.figure()
#x軸, y軸にラベル付け
plt.xlabel("epoch")
plt.ylabel(input_csv.keys()[2])
#プロットした　進捗用なので色は白黒になるようにした　グレー変換でもいいかも
plt.scatter(fi_column_data, th_column_data, linestyle='solid', facecolor = 'k', marker = 'x', s = 15, label = "training data")
plt.scatter(fi_column_data, fiv_column_data, facecolor='None', edgecolors='k', s = 15, label = "validation data")
plt.legend()
plt.savefig("./img/2.png")
# plt.show()