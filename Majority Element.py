from typing import List

def majorityElement(nums: List[int]) -> int:
        from collections import Counter
        req_len = len(nums)/2

        num_count = Counter(nums)

        for i in num_count:
            if num_count[i] > req_len:
                return i

print(majorityElement([3,2,3]))
