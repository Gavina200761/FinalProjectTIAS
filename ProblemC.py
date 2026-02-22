"""Problem C: Remove Duplicates from Sorted Array

Given a sorted array, remove duplicates in-place such that each element appears
only once. Return the new length of the array.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int: # Function to remove duplicates from a sorted list and return the new length
    """Removes duplicates from a sorted list in-place and returns new length.

    Uses two pointers:
    - `write_index` tracks where the next unique value should be written.
    - `read_index` scans through the array.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not nums:
        return 0

    write_index = 1

    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


if __name__ == "__main__":
    raw_nums = input("Enter sorted integers separated by spaces: ").strip()
    nums = [int(x) for x in raw_nums.split()] if raw_nums else []

    new_length = remove_duplicates(nums)

    print(f"New length: {new_length}")
    print(f"Array after removing duplicates: {nums[:new_length]}")
