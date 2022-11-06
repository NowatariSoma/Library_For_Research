# 参考
# https://lemon818.com/pythop-excel/
# Python で Excel ファイルを編集（値を追加）する方法．

import openpyxl as excel
import os

#カレントディレクトリを現在のディレクトリに移動
#https://note.nkmk.me/python-script-file-path/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

wbname = "test.xlsx"
msg = "test"

wb = excel.load_workbook(wbname)
ws = wb.active

# 書き込み処理
ws["C5"] = msg

wb.save(wbname)