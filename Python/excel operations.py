import pandas as py
import numpy as num
import xlsxwriter
import xlrd
from xlsxwriter import workbook

data = ['satya','akhil','santosh']
data2 = [497,498,499]
data3 = [2,1,3]
maths = [89,67,76]
eng = [87,77,96]
total = []
df = py.DataFrame({'NAME':data , "ROLL":data2 , "RANK":data3 , "MATHS":maths,'ENGLISH':eng})
df.to_csv(f'C:\\Users\\Admin\\Desktop\\student.csv',index=False)

dread = py.read_csv(f'C:\\Users\\Admin\\Desktop\\student.csv',index_col=False)
dread['TOTAL'] = dread['MATHS'] + dread['ENGLISH']
dread.to_csv(f'C:\\Users\\Admin\\Desktop\\student.csv',index=False)