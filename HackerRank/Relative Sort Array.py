import collections

def relativeSortArray(arr1, arr2):
    c = collections.Counter(arr1)
    # c only has the unused elements since they were not popped
    res = [[i]*c.pop(i) for i in arr2] 
    # res returns a list of lists because of [i], this is because
    # in a list comp each val would for 1 would have been added to itself rather than appended to a list
    # and would look like this
    # [3,4,3,12]
    # return a flattened list
    return [lis for sublist in res for lis in sublist] + sorted(c.elements())


print(relativeSortArray([1,1,4,4,2,1,2,3,4],[1,2,3,4]))


