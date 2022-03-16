import xlrd

book = xlrd.open_workbook("C:\\Users\\Asif\\Desktop\\Book1.xls")

print ("The number of worksheets is", book.nsheets)

print ("Worksheet name(s):", book.sheet_names())

sh = book.sheet_by_index(0)

print(sh.name, sh.nrows, sh.ncols)

print ("Cell D30 is", sh.cell_value(rowx=2, colx=1))

for rx in range(sh.nrows):

    print (sh.row(rx))