import xlwt
import xlrd

workbook = xlrd.open_workbook('C:\\Users\\Asif\\Desktop\\Book1.xls')
sheet = workbook.sheet_by_index(0)

data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')
for index, value in enumerate(data):
    row = sheet.row(0)

    sheet.write(0, index, "Vxcvcxv")
    print(sheet.cell_value(0, 0))

workbook.save('C:\\Users\\Asif\\Desktop\\Book1.xls')