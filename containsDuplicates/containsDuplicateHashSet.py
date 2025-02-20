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
    uniqueElements = set()

    for value in nums:
        if value in uniqueElements:
            return True
        else:
            uniqueElements.add(value)

    return False

#Difficulty: Easy
#Method: Using a Hash Set
#Time Complexity: O(n)
#Space complexity: O(n)