"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
"""

def twoSumWithSorted(nums: list[int], target: int) -> list[int]:
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()

    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = indexed_nums[left][0] + indexed_nums[right][0]

        if curr_sum == target:
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Difficulty: Easy
# Method: Using two pointers method
# Time complexity: O(nlog(n))
# Space complexity: O(n)