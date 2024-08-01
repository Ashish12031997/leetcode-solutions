from typing import List

def sumOfSquares(nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(0,n):
            if n % nums[i] == 0:
                total += nums[i] * nums[i]
        return total
                
                

sumOfSquares([2,7,1,19,18,3])
