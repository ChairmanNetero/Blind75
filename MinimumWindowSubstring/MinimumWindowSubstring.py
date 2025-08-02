"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""


def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    # Count characters in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Variables for sliding window
    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(t_count)  # Number of unique characters in t that need to be matched
    formed = 0  # Number of unique characters in current window with desired frequency

    # Dictionary to keep count of characters in current window
    window_counts = {}

    for right in range(len(s)):
        # Add character from the right to the window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the frequency of current character added equals to the
        # desired count in t then increment the formed count by 1
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try to contract the window till it ceases to be 'desirable'
        while left <= right and formed == required:
            char = s[left]

            # Save the smallest window until now
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # The character at the left pointer is no longer part of the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            # Move the left pointer ahead for the next iteration
            left += 1

    # Return the smallest window or an empty string if no such window exists
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]

# Difficulty: Hard
# Method: Using Sliding Window algorithm
# Time complexity: O(n)