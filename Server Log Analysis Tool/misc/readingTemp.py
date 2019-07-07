SmallFilePath = '/Users/Grim/Desktop/log2.txt'
BigFilePath = ''

def readData():
    file = open(SmallFilePath, 'rt')        
    data = file.readline()
    for line in file:
        print(data)
        
        #test = data.replace('form[','form [')
        #print(test)
        bufferData = data.split(']')[0]
        bufferedData = bufferData.replace('[','')
        
        print("***")
        print(bufferedData)
        print("***")
        
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