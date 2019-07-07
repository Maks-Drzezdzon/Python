def main():   
  
    classA = 0
    classB = 0
    classC = 0
    classD = 0
    a_set = set()
    b_set = set()
    c_set = set()
    d_set = set()
    def test():    
        #read all lines in the file 
        
        #loops through the file putting it in a specific pattern for the code to read
        #and sort in read_data
        with open('sl.txt', 'r') as in_file:
            
            
            for line in in_file:
                remove = line.split(';')
                bit = int(remove.split('.')[0])
                #compare 
                if bit < 126:
                    ++classA
                    a_set.add(line)
                if bit < 191 and bit > 126:
                    ++classB
                    b_set.add(line)
                if bit < 223 and bit > 191:
                    ++classC
                    c_set.add(line)
                if bit < 239 and bit > 223:
                    ++classD
                    d_set.add(line)
            
            print("set A data")   
            print("number of type A addresses found : " + classA) 
            print(a_set)
            
            print("set B data")   
            print("number of type B addresses found : " + classB) 
            print(b_set)
            
            print("set C data")   
            print("number of type C addresses found : " + classC) 
            print(c_set)
            
            print("set D data")   
            print("number of type D addresses found : " + classD) 
            print(d_set)
    #runs the code function
    test()
main()