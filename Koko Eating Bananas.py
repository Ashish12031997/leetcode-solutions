from typing import List
def minEatingSpeed(piles: List[int], h: int) -> int:
    def can_finish_all_bananas(k):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k  # Equivalent to ceil(pile / k)
        return total_hours <= h

    # Binary search for the minimum k
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if can_finish_all_bananas(mid):
            right = mid  # Try to find a smaller k
        else:
            left = mid + 1  # Increase k
    
    return left

print(minEatingSpeed([3,6,7,11],8))
