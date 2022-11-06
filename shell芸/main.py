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

print(len(check))
for i in range(1):
    print(check[i], check[i+1])
    proc = subprocess.run("python hello.py", shell=True, text=True, input = check[i]+" "+check[i+1])