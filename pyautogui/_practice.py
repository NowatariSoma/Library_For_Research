# import pandas as pd
# import pyautogui

class FUDE:
    def __init__(self):
        self.input_name()
        print(self.list_name)
        # result = self.initialize()  # 別のメソッドを呼び出し、結果を変数に代入
        # print("1 + 1 の結果は:", result)

    def input_name(self):
        n = int(input())
        list_name = [input().split() for i in range(n)]
        self.list_name = list_name

my_object = FUDE()  # 初めに実行される関数が呼び出され、他の関数も実行される
