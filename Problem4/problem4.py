from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:
    # Dictionary to store elements and their indices.
    num_indices = {}
    
    for i, num in enumerate(nums):
        # Check if the complement of num is already in the dictionary.
        complement = target - num
        print(f"num: {num}, complement: {complement}")
        if complement in num_indices:
            # If yes, return the indices of num and its complement
            print("Found complement")
            return [num_indices[complement], i]
        num_indices[num] = i
        print(f"num_indices: {num_indices}")
    
    # No solution is found, return an empty list
    return []

# Test cases
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))





