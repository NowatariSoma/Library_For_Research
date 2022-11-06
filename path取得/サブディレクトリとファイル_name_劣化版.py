import glob
import os
from natsort import natsorted

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def listup_files(path):
    yield [os.path.abspath(p) for p in glob.glob(path)]

# path = "./data"
path = "/home/nowatari/repos/datasets/research/2pulse/ejecta_raw"
folderfile = os.listdir(path)
print(folderfile)
folder = [f for f in folderfile if os.path.isdir(os.path.join(path, f))]
folder = natsorted(folder)

check = list(listup_files(path))[0]
check.sort()

for dir_path in range(len(folder)):
    print(dir_path)
    # print("dir_name : ", os.path.basename(dir_path))
    # files = list(listup_files(path))[0]
    # if len(files) > 16:
    #     print("oh_my_god")