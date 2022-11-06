import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for current, subfolders, subfiles in os.walk("./data"):
    print(f"現在のフォルダは{current}です。")
    print(f"サブフォルダは{subfolders}です。")
    print(f"サブファイルは{subfiles}です。")
    print("-------------------------------------------------------")