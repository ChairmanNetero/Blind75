"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Difficulty: Easy
# Method: Using sorted function
# Time Complexity: O(nlog(n))
# Space complexity: O(1)
