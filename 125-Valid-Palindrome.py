class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        comparison = ''.join(i.lower() for i in s if i.isalnum())
        return comparison == comparison[::-1]