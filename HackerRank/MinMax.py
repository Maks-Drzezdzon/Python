class Solution:
    def answer(a: list) -> list:
        answer = []
        
        numbers = sorted(a)
            
        min_val = sum(numbers) - numbers[-1]
        max_val = sum(numbers) - numbers[0]
        print(min_val,max_val)
        
    answer([3,2,1,1,4,2,5])