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
    if len(s) != len(t):
        return False

    counterS, counterT = {}, {}

    for i in range(len(s)):
        counterS[s[i]] = 1 + counterS.get(s[i], 0)
        counterT[t[i]] = 1 + counterT.get(t[i], 0)

    for c in counterS:
        if counterS[c] != counterT.get(c , 0):
            return False
    return True

# Difficulty: Easy
# Method: Using Two Hash tables
# Time Complexity: O(n+m) where n is length of s and m is length of t.
# Space complexity: O(1)