class Solution:
    # this question was so poorly explained that it took longer to figrue out what was asked than find a good solution
    
    
    def peakIndexInMountainArray(self, A: list[int]) -> int:
        '''
        python rounds dpown not up in this case hence this wont find peak
        however this is a great way to find the most common element in an array
        assuming there is only one
        with
        a = sorted(array) 
        a[len(array)//2]
        '''
        
        return A[len(A)//2]
    

    def peakIndexInMountainArrayV2(self, A: list[int]) -> int:
        '''
        this is why the question is poorly explained
        since the peak is the highest number, y'know the peak
        just itterate through it till you find it
        this sounds terrible because its O(n!)
        on leetcode it runs at 80ms
        '''
        
        i=0
        while A[i] < A[i + 1]:
            i += 1
        return i
    
    def peakIndexInMountainArrayV3(self, A: list[int]) -> int:
        '''
        Binary searching it the fastest but it was my recent attempt because i didnt understand what the question was asking for
        the target is replaced by a range
        if guess is the peak and being the biggest number 
        is it bigger than the number after it and before it ? if yes, then return it
        if not
        add one to the index and go again
        else
        do the reverse by setting low to mid + 1
        on leetcode it runs at 63 ms
        '''
        low = 0
        high = len(A) - 1
        
        while low <= high:
            mid = (low + high) // 2 # rounds down
            guess = A[mid]
            # without target, target now being between low and high
            # A[mid - 1] and A[mid + 1]
            if A[mid - 1] < guess and guess > A[mid + 1]:
                return mid
            
            # if guess is higher than
            if guess > A[mid + 1]:
                high = mid
            else:
                low = mid + 1
                
        return None