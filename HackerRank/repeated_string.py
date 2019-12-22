# Complete the repeatedString function below.
def repeatedString(s, n):
    
    
    # e.g
    # s=aba n=10
    # count a in string = 2
    # *
    # n=10//len(s)
    # 10//3 = 3
    #
    # 2 * 3 = 6
    # +
    # remeinder of s
    # s[:n % len(s)]
    # 10 % 3 = 1
    # s[:1] content looks like ['a'], it is not inclusive
    # s.count('a') = 1
    # 6 + 1 = 7
    # answer is 7
    
    
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')

    # at first i wanted to do this with just maths by counting the number of times s can fit into n
    # however the restraint is you have to actually count 'a' so if you get input of x you have 0
    # you cant find that without coutning it in the string
    
