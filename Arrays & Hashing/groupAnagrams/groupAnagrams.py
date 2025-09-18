"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagramsDictionary = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)
        anagramsDictionary[key].append(s)

    return list(anagramsDictionary.values())

# Difficulty: Medium
# Method: Using a hash Map to group strings with the same key
# Time complexity: O(n*m) where n is the number of strings and m is the average string length
# Space complexity: O(n*m) the number of characters stored in total