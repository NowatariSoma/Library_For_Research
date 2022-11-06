import os
from natsort import natsorted
os.chdir(os.path.dirname(os.path.abspath(__file__)))

path  = "./data"
folderfile = os.listdir(path)
folder = [f for f in folderfile if os.path.isdir(os.path.join(path, f))]
folder = natsorted(folder)

print(folder)