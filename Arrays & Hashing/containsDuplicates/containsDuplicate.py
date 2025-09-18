"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

def containsDuplicate( nums: list[int]) -> bool:
    seen = {}

    for value in nums:
        if value not in seen:
            seen[value] = 1
        else:
            return True

    return False

# Time complexity: O(n)