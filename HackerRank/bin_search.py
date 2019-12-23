
def binSearch(arr, target) -> int:
    # sort array incase its not
    array = sorted(arr)
    # set high low for going between start and mid
    low = 0
    high = len(array) - 1
    
    while low <= high:
        # set mid to be halfway between low and high
        # mid index
        mid = (low + high) // 2
        # get number at index mid
        guess = array[mid]
        if guess == target:
            # if guess == target well... you found it
            return mid
        
        if guess > target:
            # if guess is bigger than target
            # it means its too high
            # set high to mid - 1 to lower it
            # and reroll
            high = mid - 1
        else:
            # do the opposite
            # add 1 because its too low
            low = mid + 1
    
    return None

# returns index
print(binSearch([1,2,3,4,5,6,7,8,9], 9))