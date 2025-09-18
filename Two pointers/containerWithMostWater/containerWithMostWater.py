"""
You are given an integer array heights where heights[i] represents the height of the ith bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

"""


def maxArea(heights: list[int]) -> int:
    i = 0
    j = len(heights) - 1
    max_area = 0

    while i < j:
        length = min(heights[i], heights[j])
        area = length * (j - i)
        max_area = max(max_area, area)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1

    return max_area

# Difficulty: Medium
# Method: Using two pointers
# Time complexity: O(n)