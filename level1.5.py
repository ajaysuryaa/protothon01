from itertools import permutations
import xlrd
filelocation ="C:\Users\hp\Desktop\ProtoThon#01\word.xlsx"
workbk = xlrd.open_workbk(filelocation)
sheet = workbk.sheet_by_index(0)
filelocation = ""
a="ProtoSem"
x=permutations(a)
total_rows = sheet.nrows
for i in x:
    str = ''.join(i)
    for j in range(total_rows):
        if str.lower() == sheet.cell_value(j,0):
            print(str)
