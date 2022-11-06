# 参考
# https://lemon818.com/pythop-excel/
# Python で Excel ファイルを読み込む方法．

import openpyxl as excel
import os

#カレントディレクトリを現在のディレクトリに移動
#https://note.nkmk.me/python-script-file-path/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

wbname = "test.xlsx"
wb = excel.load_workbook(wbname)

# シート単位にループ
for sheet in wb.sheetnames: 
    print("シート名:" + sheet)
    ws = wb[sheet]
    # 行単位にループ
    for row in ws.rows:
        # 列単位にループ
        for cell in row:
            print("行:" + str(cell.row) + " 列:" + str(cell.column))
            print("値:" + str(cell.value))