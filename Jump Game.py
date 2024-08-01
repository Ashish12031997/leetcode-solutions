from typing import List

def canJump(nums: List[int]) -> bool:
    cj = False
    last_index = len(nums) - 1
    n=1
    if last_index ==0:
            return True
    while n <= last_index:
        if nums[n-1] == 0:
            cj = False
            break
        max_index = max((x for x in nums[n:n+nums[n]] if x), default=0)
        if n+max_index >= last_index:
            cj = True
            break
        elif max_index == 0:
            cj = False
            break    
        else:
            n = n + max_index
        
    return cj


j = canJump([0,1])
print(j)
