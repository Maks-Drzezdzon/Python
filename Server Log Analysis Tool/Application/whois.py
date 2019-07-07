from ipwhois import IPWhois
from pprint import pprint

#usefull link 
#https://pypi.org/project/ipwhois/
#
file_path = '..//Application/sorted_log.txt'
whois_read = open(file_path , 'r')

def whois():
    try:
        read_file = whois_read.readlines()
        for data in read_file:
            
            #splits the log at item 5 which is the ip address
            isolate_ip_address = data.split(' ')[5]
            #strip the [] from the ip address
            strip_excess_char = isolate_ip_address.strip('[') 
            
            strip_excess_char_2 = strip_excess_char.replace(']','')
            #strip any new lines from the file
            ip = strip_excess_char_2.strip()
            
            #store the isolated ip
            store_ip = ip
            #use the IPWhois method to check the ip stored in store_ip
            querry_ip = IPWhois(store_ip)
            #store result from look up
            results = querry_ip.lookup_whois()
            #print out results
            pprint(results.lookup())
            #break stops it going through all the ips for now
            data_string = "{}"
            #printout the data using the format above
            #append the output to a new file called sortedLog
            #print(data_string.format(day,month,day_of_month,time_stamp,year, "["+ip_Address))
            print(data_string.format(results),file = open('whois.txt' , 'a'))
            
    except Exception as e:
            print (e)
        
whois()
whois_read.close()