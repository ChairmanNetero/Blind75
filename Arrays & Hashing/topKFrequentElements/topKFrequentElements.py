"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for value in nums:
        count[value] = 1 + count.get(value, 0)
    for value, i in count.items():
        freq[i].append(value)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# Difficulty: Medium
# Method: Using Bucket sort and Hash map to keep count of each element
# Time complexity: O(n)
# Space complexity: O(n)