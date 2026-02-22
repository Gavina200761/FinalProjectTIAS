"""Problem A: Two Sum

Given an array of integers and a target sum, find two numbers that add up to the
target and return their indices.
"""

from typing import List, Optional, Tuple # Importing necessary types for type hints


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]: # Function to find two indices in nums that add up to target
    """Return indices of two numbers in nums that add up to target.

    Uses a hash map to store seen values and their indices.
    Time complexity: O(n)
    Space complexity: O(n)

    Returns:
        A tuple of indices (i, j) if a pair exists, otherwise None.
    """
    seen = {} # Dictionary to store numbers and their indices

    for i, num in enumerate(nums): # Iterate through the list of numbers
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

    return None


if __name__ == "__main__": 
    # Simple interactive runner
    raw_nums = input("Enter integers separated by spaces: ").strip()
    nums = [int(x) for x in raw_nums.split()] if raw_nums else []
    target = int(input("Enter target sum: ").strip())

    result = two_sum(nums, target)
    if result is None:
        print("No two numbers add up to the target.")
    else:
        print(f"Indices: {result[0]}, {result[1]}")
