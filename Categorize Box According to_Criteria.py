def rotate(nums, k):
    n = len(nums)
    k %= n  # In case k is larger than n
    nums.reverse()  # Step 1: Reverse the entire array
    reverse(nums, 0, k-1)  # Step 2: Reverse the first k elements
    reverse(nums, k, n-1)  # Step 3: Reverse the elements from k to the end

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
