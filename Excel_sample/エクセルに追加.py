import openpyxl as excel
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wbname = "test.xlsx"
msg = "test"

wb = excel.load_workbook(wbname)
ws = wb.active

# 書き込み処理
ws["C5"] = msg

wb.save(wbname)