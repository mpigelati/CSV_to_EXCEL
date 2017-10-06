import os
import  glob
import csv
import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

from xlsxwriter.workbook import Workbook
#########
#csv_fd= open("CSVFile_2kb.csv",'r',)

#error:- UnicodeDecodeError: 'utf-8' codec can't decode byte 0xae in position 265: invalid start byte
#########

with  open("CSVFile_11kb.csv",'r',encoding='utf-8',errors="ignore") as fd:
    for line in csv.reader(fd):
        ws.append(line)
wb.save("CSVFile_11kb.xlsx")






