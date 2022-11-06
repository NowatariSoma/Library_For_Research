import openpyxl as xl

wbname = "excel_output/output.xlsx"
wb_out = xl.Workbook()
ws_out = wb_out.active

for i in range(10):
    for j in range(10):
        ws_out.cell(row=i+1,column=j+1).value = str(i) + str(j)

wb_out.save(wbname)