from collections import Counter
def makeAnagram(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    
    c = a - b
    #print(c)
    d = b - a
    #print(d)
    e = c + d
    #print(e)
    return len(list(e.elements()))
    


s1="showman"
s2="woman"
print(makeAnagram(s1,s2))