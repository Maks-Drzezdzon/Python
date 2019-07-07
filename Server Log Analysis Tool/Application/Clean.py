import os

def main():
    try:
        if os.path.exists("ip_count.txt"):
            os.remove("ip_count.txt")
        else:
            print('File does not exists')
            
        if os.path.exists("unique.txt"):
            os.remove("unique.txt")
        else:
            print('File does not exists')
    
        if os.path.exists("sorted_log.txt"):
            os.remove("sorted_log.txt")
        else:
            print('File does not exists')
    
        if os.path.exists("counted_ips.txt"):
            os.remove("counted_ips.txt")
        else:
            print('File does not exists')
    
        if os.path.exists("sl.txt"):
            os.remove("sl.txt")
        else:
            print('File does not exists')
            
        if os.path.exists("tmp.txt"):
            os.remove('tmp.txt')
        else:
            print('File does not exists')
    
        if os.path.exists("ips.txt"):
            os.remove('ips.txt')
        else:
            print('File does not exists')
    
        if os.path.exists("log.csv"):
            os.remove('log.csv')
        else:
            print('File does not exists')
    
        if os.path.exists("unique.csv"):
            os.remove('unique.csv')
        else:
            print('File does not exists')
        
            
            
    except Exception as e:
        print(e)