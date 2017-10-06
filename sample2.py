from openpyxl import Workbook
import csv


wb = Workbook()
ws = wb.active
with open('CSVFile_11kb.csv', 'r',encoding='utf-8',errors="ignore") as f:
    for row in csv.reader(f):
        ws.append(row)

wb.save('name.xlsx')