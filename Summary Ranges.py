from typing import List
def summaryRanges(nums: List[int]) -> List[str]:
    ranges = []
    if not nums:
        return ranges
    
    start = nums[0]  # Initialize the start of the first range
    
    for i in range(1, len(nums)):
        # If the current number is not consecutive, close off the current range
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            start = nums[i]  # Start a new range
    
    # Add the final range
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")
    
    return ranges

print(summaryRanges([0,2,3,4,6,8,9]))
