class Solution:
    def peakIndexInMountainArray(self, A: list[int]) -> int:
        return A[int(len(A)/2)]
    

    def peakIndexInMountainArrayV2(self, A: list[int]) -> int:
        i=0
        while A[i] < A[i + 1]:
            i += 1
        return i