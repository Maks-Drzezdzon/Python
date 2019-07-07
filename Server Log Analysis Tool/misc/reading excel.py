import xlrd
import xlwt
#open excel file
workbook = xlrd.open_workbook('test_excel.xlsx')

print (workbook.sheet_names())

#get a worksheet from a excel file
worksheet = workbook.sheet_by_name('Sheet1')

   
print ('cell with value 2,0 is ' + worksheet.cell_value(2,0))



#iterate over each worksheet in excel file
worksheets = workbook.sheet_names()
for worksheet_name in worksheets:
    worksheet = workbook.sheet_by_name(worksheet_name)
    print (worksheet)

#iterate over each row in excel file
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
curr_row = -1
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    print (row)
  
#take cell contents of each row of excel file
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    print ('Row:', curr_row)
    curr_cell = -1
    
while curr_cell < num_cells:
    curr_cell += 1
    #Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    cell_type = worksheet.cell_type(curr_row, curr_cell)
    cell_value = worksheet.cell_value(curr_row, curr_cell)
    print (' ', cell_type, ':', cell_value)
    