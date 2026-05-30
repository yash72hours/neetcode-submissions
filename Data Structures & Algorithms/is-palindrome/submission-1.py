class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())
        x = len(s)//2

        for i in range(x):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True