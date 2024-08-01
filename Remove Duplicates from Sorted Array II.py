from typing import List
from collections import Counter


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    k = len(nums)
    while i < k:
        count = Counter(nums)
        if count[nums[i]] > 2:
            count[nums[i]] -= 1
            nums.pop(i)
            k -= 1
            i = i - 1
        i = i + 1
    return k


p = removeDuplicates([1, 1, 1, 2, 2, 3])
print(p)
