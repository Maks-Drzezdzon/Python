from ipwhois import IPWhois
from pprint import pprint


def whois(ip):
        try:
            #use the IPWhois method to check the ip stored in store_ip
            querry_ip = IPWhois(ip)
            #store result from look up
            results = querry_ip.lookup_whois()
            #print out results
            pprint(results)
            #break stops it going through all the ips for now
            data_string = "{}"
            #printout the data using the format above
            #append the output to a new file called sortedLog
            #print(data_string.format(day,month,day_of_month,time_stamp,year, "["+ip_Address))
            print(data_string.format(results),file = open('whois.txt' , 'a'))
        except Exception as e:
                print (e)
       
        
whois()
