#file 2

#call the fix pattern method to format the file
#fix_pattern.fixPattern()
#path for file 
file_path = '/Users/Grim/Documents/GitHub/DDoS-Server-Log-Scanner/Application/tmp.txt'

#open file for reading
tmp_file_cleaned = open(file_path , 'r')
sorted_file = open('sorted_log.txt' , 'w')

def readData():
    #read all lines in the file 
    read_file = tmp_file_cleaned.readlines() 
    #read data in file readFile
    #store each line in variable data
    #loop through the lines in read_file variable
    for data in read_file:    
        #these actions will be performed on each line as its being passed through the code
        strip_data_new_line = data.strip()  
        #extract and store data from the stripped line in the locations described in []     
        day = strip_data_new_line.split(' ')[0]
        
        month = strip_data_new_line.split(' ')[1]
        
        day_of_month = strip_data_new_line.split(' ')[2]
        
        time_stamp = strip_data_new_line.split(' ')[3]
        
        year = strip_data_new_line.split(' ')[4]
        
        ip_address = strip_data_new_line.split(' ')[7]
        
        #structure the output in this pattern
        data_string = "{} {} {} {} {} {}"
        #printout the data using the format above
        #append the output to a new file called sortedLog
        #print(data_string.format(day,month,day_of_month,time_stamp,year, "["+ip_Address))
        print(data_string.format(day,month,day_of_month,time_stamp,year, "["+ip_address),sorted_file = open('sorted_log.txt' , 'a'))
#runs the code function         
readData()
#close file when done with operation
tmp_file_cleaned.close() 
sorted_file.close() 