work_book = load_workbook(r'G:\Desktop\工作簿1.xlsx')
print(work_book.sheetnames)
sheet_data = work_book['题目一4450-4469']
print(sheet_data)