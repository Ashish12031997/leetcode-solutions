from typing import List
 
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k%len(nums)
    nums[:] = nums[-k:] + nums[:-k]
nums = [1,2,3,4,5,6,7,8]
rotate(nums, 4)
