def count_analogous_arrays(differences, lowerBound, upperBound):
    valid_arrays_count = 0
    
    for a0 in range(lowerBound, upperBound + 1):
        valid = True
        current_value = a0
        
        for diff in differences:
            current_value += diff
            if current_value < lowerBound or current_value > upperBound:
                valid = False
                break
        
        if valid:
            valid_arrays_count += 1
    
    return valid_arrays_count

# Example usage:
differences = [-2, -1, -2, 5]  # Example differences array
lowerBound = 3
upperBound = 10
result = count_analogous_arrays(differences, lowerBound, upperBound)
print(result)  # This will print the number of valid arrays
