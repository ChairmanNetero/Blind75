"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
"""


def longestConsecutive(self, nums: list[int]) -> int:
    my_set = set(nums)
    max_length = 0

    for n in nums:
        if (n - 1) not in my_set:
            length = 0
            while (n + length) in my_set:
                length += 1
                max_length = max(max_length, length)

    return max_length

# Difficulty: Medium
# Method: By checking elements which are the beginning of a sequence (elements that don't have previous elements in the list)
# Time complexity: O(n)