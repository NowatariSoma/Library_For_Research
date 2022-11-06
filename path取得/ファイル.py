import glob
import os
import subprocess
from subprocess import PIPE

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# os.makedirs("image", exist_ok = True)

def listup_files(path):
    yield [os.path.abspath(p) for p in glob.glob(path)]

check = list(listup_files("../frame/*"))[0]
check.sort()
