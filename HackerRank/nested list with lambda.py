students=[]
lowest =[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students += [[name,score]]
        sorted(students,key=lambda x:x[1])

        
    lowest.append(students)

    print (sorted(lowest))
    
            

        #for student in students:
            #for name , score in student:
