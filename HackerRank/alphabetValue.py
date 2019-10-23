def solution(S):
    '''
    this code was meant to return an uppercase letter if the input string had both an upper and lowercase version of it
    each letter was given a score based on its place on the alphabet the highest placed letter is always picked
    if conditions arent met print NO
    '''
    alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9,
    'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16,
    's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    keys_list = list(alphabet.keys())
    values_list = list(alphabet.values())
    keys=list()
  
    for ele in S:
        if ele.isupper():
            
            
            lowerCase = ele.lower().strip()
            
            #print(lowerCase)
            
            if lowerCase in S:
                key = alphabet[lowerCase]
                keys.append(key)
              
    
    if len(keys) == 0:
        return "NO"
    return keys_list[values_list.index(max(keys))].upper()

            
print(solution('abc'))