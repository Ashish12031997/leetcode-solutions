def count_valid_combinations(jeans, shoes, skirts, tops, budget):
    from itertools import product

    # Generate all possible sums for jeans and shoes
    jeans_shoes = [j + s for j, s in product(jeans, shoes)]

    # Generate all possible sums for skirts and tops
    skirts_tops = [k + t for k, t in product(skirts, tops)]

    # Sort the skirts_tops array to enable binary search
    skirts_tops.sort()

    valid_combinations_count = 0

    # Iterate over all possible sums of jeans_shoes
    for js_price in jeans_shoes:
        remaining_budget = budget - js_price

        # Count the number of valid skirts_tops combinations that are <= remaining_budget
        left, right = 0, len(skirts_tops) - 1
        while left <= right:
            mid = (left + right) // 2
            if skirts_tops[mid] <= remaining_budget:
                left = mid + 1
            else:
                right = mid - 1

        valid_combinations_count += left  # All items from 0 to left-1 are valid

    return valid_combinations_count


# Example usage:
jeans = [2, 3]
shoes = [4]
skirts = [2, 3]
tops = [1, 2]
budget = 10

result = count_valid_combinations(jeans, shoes, skirts, tops, budget)
print(result)  # This will print the number of valid combinations
