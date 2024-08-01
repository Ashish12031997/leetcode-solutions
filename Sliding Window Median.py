import heapq

def medianSlidingWindow(nums, k):
    def get_median():
        if k % 2 == 0:
            return (left[0] * -1 + right[0]) / 2
        else:
            return left[0] * -1

    left, right = [], []
    
    for i in range(k):
        heapq.heappush(left, -nums[i])
    
    for i in range(k // 2):
        heapq.heappush(right, -heapq.heappop(left))
    
    medians = [get_median()]
    
    for i in range(k, len(nums)):
        num_out = nums[i - k]
        num_in = nums[i]
        
        if num_out <= -left[0]:
            left.remove(-num_out)
            heapq.heapify(left)
        else:
            right.remove(num_out)
            heapq.heapify(right)
        
        if num_in <= -left[0]:
            heapq.heappush(left, -num_in)
        else:
            heapq.heappush(right, num_in)
        
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        if len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))
        
        medians.append(get_median())
    
    return medians

# Example usage:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(medianSlidingWindow(nums, k))
