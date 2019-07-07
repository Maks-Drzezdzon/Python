SmallFilePath = '/Users/Grim/Desktop/log.txt'

file = open(SmallFilePath, 'rt')
data = file.readline()

def readData(): 
    file = open(SmallFilePath, 'rt')
    data = file.readline()
    print(data)

    bufferData = data.split(']')[0]
    bufferedData = bufferData.replace('[','')
    
    WeekDay = bufferedData.split(' ')[0]
    Month = bufferedData.split(' ')[1]
    DayOfMonth = bufferedData.split(' ')[2]
    TimeStamp = bufferedData.split(' ')[3]
    Year = bufferedData.split(' ')[4]

    print(WeekDay)
    print(Month)
    print(DayOfMonth)
    print(TimeStamp)
    print(Year)
    
    bufferAddress = data.split(']')[2]
    bufferedAddress = bufferAddress.replace('[','')
    IpAddress = bufferedAddress.split(' ')[2]
    print(IpAddress)
    return;  

readData()

"""
SmallFilePath = '/Users/Grim/Desktop/log.txt'
with open(SmallFilePath , 'rt') as file:
    while True:
#file = open(SmallFilePath, 'rt')
        data = file.readline()
        print(data)
        
        newFilePath = '/Users/Grim/Desktop/CleannedLog.txt'
        title = 'CleannedLog'
        days = open(newFilePath , 'a')
        #test = data.replace('form[','form [')[0]
        bufferDate = data.split(']')[0]
        bufferedDate = bufferDate.replace('[','')
        days.write(bufferedDate)
        days.close()
     
        if not data:
            break
"""