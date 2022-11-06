import os
from natsort import natsorted

os.chdir(os.path.dirname(os.path.abspath(__file__)))

data_path = "/home/nowatari/repos/datasets/research/2pulse/ejecta_raw/"

folderfile = os.listdir(data_path)
folder = [f.path for f in os.scandir(data_path) if f.is_dir()]
folder = natsorted(folder)

for dir_path in folder:
    print(dir_path)
    tmp = [f.path for f in os.scandir(dir_path) if f.is_file()]
    print(tmp)
    print("---------------------------------")