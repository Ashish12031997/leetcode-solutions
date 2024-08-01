def minimalHeaviestSetA(nums):
    nums.sort(reverse=True)
    total = sum(nums)
    for i in range(1, len(nums)):
        if sum(nums[:i]) > total - sum(nums[:i]):
            return nums[:i]
    return []
 
print(minimalHeaviestSetA([3, 7, 5, 6, 2]))
