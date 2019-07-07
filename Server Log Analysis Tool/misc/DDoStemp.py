import re

def readData():
    SmallFilePath = '/Users/Grim/Desktop/log.txt'
    
    file = open(SmallFilePath , 'r')
    readFile = file.readlines()
    print(readFile)
    file.close()
    
        
    for data in readFile:
        
        newData = data.replace('form[','form [')
        sortData = newData.replace('form ', '\n')
        sortedData = sortData.replace(' [ ', '')
        print(sortedData)
        file.close()
        return;
readData()
"""
SmallFilePath = '/Users/Grim/Desktop/log.txt'
log = open(SmallFilePath , 'r')
readFile = log.readlines()
    
def test_split(log, begin = '[', end = 'form['):  
    
    logList = []  
    holdString = ''  
    for char in log:  
        if char == begin:  
            holdString = ''  
        holdString += char  
        if char == end:  
            logList.append(holdString)
            print(holdString)
    return;

test_split(readFile)
log.close()
"""