import os
from collections import Counter
import re
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xlsxwriter


def main():
    #path for file
    file_path = '..//Application/log.txt'  
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
            #fix_pattern = data.replace('form','\n ')
            
            #replaced old method with regular expression
            #substitutes the from word with a from sapce that prints 
            #text to a new line without me having to juggle around anything
            fix_pattern = re.sub('form','form ', data)
            
            
            #formats and removes extra new lines
            #format_pattern = fix_pattern.replace(' \n', '')
            #writes formatted data to file
            
            tmp_file.write(fix_pattern)
    #runs the code function
    fixPattern()
    tmp_file.close()
    log_file.close()
    
    #file 2
    
    #call the fix pattern method to format the file
    #fix_pattern.fixPattern()
    #path for file 
    file_path = '..//Application/tmp.txt'
    
    #open file for reading
    tmp_file_cleaned = open(file_path , 'r')
    sorted_file = open('sorted_log.txt' , 'w')
    time_format_file = open('sl.txt' , 'w')
  
    
    #formats the data into a structure for other functions to read
    def readData():
        try:
            #read all lines in the file 
            read_file = tmp_file_cleaned.readlines() 
            #read data in file readFile
            #store each line in variable data
            #loop through the lines in read_file variable
            for data in read_file:    
                #these actions will be performed on each line as its being passed through the code
                strip_data_new_line = data.strip()  
                replace_char = strip_data_new_line.replace(']','')
                replace_char_2 = replace_char.replace('[','')
                #extract and store data from the stripped line in the locations described in []     
                #day = replace_char_2.split(' ')[0]
                
                
                month = replace_char_2.split(' ')[1]
                day_of_month = replace_char_2.split(' ')[2]
                time_stamp = replace_char_2.split(' ')[3]
                year = replace_char_2.split(' ')[4]
                ip_address = replace_char_2.split(' ')[7]
                #print(ip_address)
                #structure the output in this pattern
                data_string = "{} {} {} {} {}"
                #printout the data using the format above
                #append the output to a new file called sortedLog
                #has to be appended else it will overwrite the same line over and over 
                print(data_string.format(year+',',month+',',day_of_month,time_stamp,';'+ip_address),file = open('sl.txt' , 'a'))
        except Exception as e:
                print (e)
        
    
            
    #runs the code function         
    readData()
    
    
    time_file_path = '..//Application/sl.txt'
    
    #open file for reading
    time_fix = open(time_file_path , 'r')
    
    
    def fix():
        try:
            read_file = time_fix.readlines() 
            
            for data in read_file:
                time_format = data.replace(', ','-')
                time_format_2 = time_format.replace('; ', ';')
                
                hold = time_format_2.replace('\n','')
                
                data_string = "{}"
                print(data_string.format(hold),file = open('sorted_log.txt', 'a'))
        except Exception as e:
                print (e)
    fix()
    #close file when done with operation
    tmp_file_cleaned.close() 
    sorted_file.close()
    time_format_file.close() 
    time_fix.close()
    
    
    CreateIpList_file_path = '..//Application/sorted_log.txt'
    
    #open file for reading
    CreateIpList_tmp_file_cleaned = open(CreateIpList_file_path , 'r')
    
    def CreateIpList():
        try:
            #read all lines in the file 
            read_file = CreateIpList_tmp_file_cleaned.readlines() 
            #read data in file readFile
            #store each line in variable data
            #loop through the lines in read_file variable
            for data in read_file:    
                #these actions will be performed on each line as its being passed through the code
                strip_data_new_line = data.strip()  
                #extract and store data from the stripped line in the locations described in []     
        
                ip_address = strip_data_new_line.split(' ')[2]
                
                #structure the output in this pattern
                data_string = "{}"
                #printout the data using the format above
                #append the output to a new file called sortedLog
                
                print(data_string.format(ip_address),file = open('ips.txt' , 'a'))
        except Exception as e:
                print (e)
                
    #runs the code function         
    CreateIpList()
    #close file when done with operation
    CreateIpList_tmp_file_cleaned.close() 
    
    #this section deals with counting unique ips and preparing that data
    
    #all_ips = open ('ips.txt' , 'r')
    #unique_ips = open ('unique.txt' , 'w')
    
    def Sort():
        try:
            # create datastructures to hold data
            seen = set()
            unique = set()
            
            #open both ips and unqie file and iterate over data
            with open('ips.txt') as infile:
                with open('unique.txt', 'w') as outfile:
                    for line in infile:
                        #sequance chech if line is in set called seen
                        #if not add it to set called unique
                        if line not in seen:
                            outfile.write(line)
                            unique.add(line)
                            seen.add(line)
        except Exception as e:
                print (e)
                      
                
        #open files for processing
        all_ips = open('ips.txt' , 'r+')
        unique_ips = open('unique.txt' , 'r')
        
        #count ips
        ip_count = Counter (all_ips)
        #used for debugging
        #print(ip_count)
        
        #count unique ips and print to file
        for data in unique_ips:
            print((data ,ip_count[data] ), file = open('ip_count.txt' , 'a')) #file contains unique ips and how many times they occured in 
        
    Sort()
    #close files after everything is finished
    #all_ips.close()
    #unique_ips.close()
    #remove unused files
    os.remove('ips.txt')
    os.remove('tmp.txt')
    #call the unique function ot find and sort the ips and count occurances
    file_unique = open ('ip_count.txt','r')
    
    def Unique():
        try:
            read_file = file_unique.readlines()  
            #read data in file readFile
            #store each line in variable data
            #loop through the lines in read_file variable
            for data in read_file:    
                #these actions will be performed on each line as its being passed through the code
                strip_data_new_line = data.strip()  
                #extract and store data from the stripped line in the locations described in [] 
                
                strip_characters = strip_data_new_line.replace("('","")
                
                strip_characters_2 = strip_characters.replace(")","")
                #an extra \ has to be added as a regular expressin argument because \n is considered a new line when there is no new line
                #it is a literal \n in the text so it must be treated as a regular expression
                remove_newline_character = strip_characters_2.replace("\\n'",'')
                
                remove_delimiter = remove_newline_character.replace(';','')
                ip_address = remove_delimiter.split(' ')[0]
                #print is used for debugging output
                #print(ip_address)
                
                number_of_occurances = remove_newline_character.split(' ')[1]
                
        
                #print(ip_address)
                #structure the output in this pattern
                data_string = "{} {}"
                #printout the data using the format above
                #append the output to a new file called sortedLog
               
                #this file contains the stripped data from ip_count.txt
                print(data_string.format(ip_address,number_of_occurances),file = open('counted_ips.txt' , 'a')) 
        except Exception as e:
                print (e)
            
    #runs the code function         
    Unique()
    
    file_unique.close() 
    os.remove('ip_count.txt')
    
    
    #now convert data to csv format
    def ToCSV():
        try:
            #open file
            with open('sorted_log.txt', 'r') as in_file:
                #strip data
                stripped = (line.strip() for line in in_file)
                #split stripped data on delimiter ; previously added
                lines = (line.split(";") for line in stripped if line)
                #open a new file for saving this output
                with open('log.csv', 'w') as out_file:
                    #assign variable to writer
                    writer = csv.writer(out_file)
                    #name rows
                    #because there are only 2 fields that can come from the ; delimiter only two rows must be named
                    writer.writerow(('Time', 'Address'))
                    #write out data
                    writer.writerows(lines)
    
            
            #same as above
            with open('counted_ips.txt', 'r') as in_file:
                stripped = (line.strip() for line in in_file)
                lines = (line.split(",") for line in stripped if line)
                with open('unique.csv', 'w') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow(('Unique_IP', 'Occurrences'))
                    writer.writerows(lines)
        except Exception as e:
                print (e)     
            
    ToCSV()
    
main()