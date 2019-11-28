import collections

def favGenres(userSongs, songGenres):
    output={}
    for i in userSongs:
        list=userSongs[i]
        count=collections.defaultdict(int)
        for j in list:
            for k,v in songGenres.items():
                if j in v:
                    count[k]+=1

        print(count)
        output[i]=[key for key,val in count.items() if val ==max(count.values())]
                
    
    return output