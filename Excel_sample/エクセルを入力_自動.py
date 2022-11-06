import openpyxl as xl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wbname = "excel_input/1.xlsx"
wb = xl.load_workbook(wbname)

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