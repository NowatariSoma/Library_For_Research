import os
from natsort import natsorted

os.chdir(os.path.dirname(os.path.abspath(__file__)))

data_path = "/home/nowatari/repos/datasets/research/2pulse/ejecta_raw/"

folderfile = os.listdir(data_path)
folder = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
folder = natsorted(folder)

print(folder)

for i in range(len(folder)):
    tmp = [f.path for f in os.scandir(data_path + folder[i]) if f.is_file()]
    print(tmp)
    print("---------------------------------")