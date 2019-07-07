#file 1

#path for file
file_path = '/Users/Grim/Documents/GitHub/DDoS-Server-Log-Scanner/Application/log1.txt'  
#open file for reading
log_file = open(file_path , 'r')
tmp_file = open('tmp.txt','w') # this file is only for storage it is removed after the operation is finished in readData

def fixPattern():    
    #read all lines in the file 
    read_file = log_file.readlines()    
    #loops through the file putting it in a specific pattern for the code to read
    #and sort in read_data
    for data in read_file:
        #hold variable for replacing value
        #replaces irrelevent form word with new line to split mashed text up
        fix_pattern = data.replace('form','\n ')
        #formats and removes extra new lines
        format_pattern = fix_pattern.replace(' \n', '')
        #writes formatted data to file
        tmp_file.write(format_pattern)
#runs the code function
fixPattern()
tmp_file.close()
log_file.close()
