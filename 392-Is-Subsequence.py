class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set = 0

        for i in s:
            while s_set < len(t) and t[s_set] != i:
                s_set += 1
            if s_set == len(t):
                return False
            s_set += 1
        return True