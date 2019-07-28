import requests
import pprint
from itertools import product

# map int , input method store in a list
a = list (map(int,input().split()))
b = list (map(int,input().split()))

# unpacks each item into a list()
s = list(*product(a,b, repeat=2))
# returns a tuple in a list
s = list(product(a,b, repeat=2))

print(s[0])




##################################
''' itertools '''

from itertools import permutations
a = list(map(str,input().split()))

size_of_output = int(a[1])
word = a[0]
answer =  list(permutations(word,size_of_output))

for ele in sorted(answer):
    print ("".join(ele))



##################################################
'''Recursion'''
# use lre_cache last recently used
from functools import lru_cache

@lru_cache(maxsize = 10)
def fibonacci(n):
    # if we have cached the value, then return it
    # f_cache = {}
    # if n in f_cache:
        # return f_cache[n]
    
    # cal the Nth term
    if n == 1:
        n = 1 
        # value = 1
    elif n == 2:
         n = 2
        # value = 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)    
    # f_cache[n] = value
    

##################################################
'''lambda + map + filter'''
# lambda do function on each passed in var
# map map function to function
function = lambda data: (data[0],2*data[1] - 2)
lis = [['a',2],['b',5],['p',9],['d',2],['t',3]]
lis1 = [[9,2],[1,5],[1,9],[1,2],[1,3]]

import statistics
func = lambda x : (statistics.mean (x[1]))
avg = [func(lis1)]
print(avg)

print(list(filter(lambda x: x > avg,lis1)))
# cast results to list and print
a = list(map(function,lis))
print(a)

