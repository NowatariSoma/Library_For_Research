import openpyxl as xl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wbname = "excel_input/1.xlsx"
wb_in = xl.load_workbook(wbname)
ws_in = wb_in.worksheets[0]

for i in range(10):
    for j in range(1):
        print(ws_in.cell(row=i+1,column=j+1).value)