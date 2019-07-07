import xlwt
#creating a new excel sheet for data dump
workbook = xlwt.Workbook()

#add a sheet to it
worksheet = workbook.add_sheet('sheet name')
#Add some values
for x in range(0, 10):
    for y in range(0,10):
        worksheet.write(x,y,x*y)
        
workbook.save('server_log.xls')