def moveZeroes(nums) -> None:
    length = len(nums)
    count = 0
    index = 0
    
    while index < length and count < length:
        if nums[index] == 0:
            nums.pop(index)
            nums.append(0)
        else:
            index += 1
        
        count += 1
        