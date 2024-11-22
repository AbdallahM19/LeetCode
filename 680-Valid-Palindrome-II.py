class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = len(s) - 1
        left = 0

        while left < right:
            if s[left] != s[right]:
                if s[left + 1:right + 1] == s[left + 1:right + 1][::-1] or s[left:right] == s[left:right][::-1]:
                    return True
                return False
            left += 1
            right -= 1

        return True