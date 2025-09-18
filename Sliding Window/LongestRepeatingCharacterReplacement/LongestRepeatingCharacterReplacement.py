"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

"""

def characterReplacement(s: str, k: int) -> int:
    longest = 0
    l = 0
    counts = [0] * 26

    for r in range(len(s)):
        counts[ord(s[r]) - 65] += 1
        while(r-l+1) - max(counts) > k:
            counts[ord(s[l]) - 65]  -= 1
            l += 1

        longest = max(longest, (r-l+1))

    return longest

# Difficulty: Medium
# Method: Using Sliding Window algorithm
# Time complexity: O(n)