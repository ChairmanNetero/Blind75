"""
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""


def isAlphaNum(c):
    return (('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9'))


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not isAlphaNum(s[l]):
            l += 1
        while r > l and not isAlphaNum(s[r]):
            r -= 1

        if (s[l].lower() != s[r].lower()):
            return False
        l, r = l + 1, r - 1

    return True

# Difficulty: Easy
# Method: two pointers (left and right)
# Time complexity: O(n)