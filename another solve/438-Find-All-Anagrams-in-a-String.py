from typing import List

class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        if len(p) > len(s):
            return result

        for i in range(len(s) - len(p) + 1):
            counting = []

            for j in range(i, i + len(p)):
                print(s[j], j)
                if s[j] in p and s[j] not in counting:
                    counting.append(s[j])

            if len(counting) == len(p):
                result.append(i)
                counting = []

        return result


sol = Solution()

s = "cbaebabacd"
p = "abc"

print(sol.findAnagrams(s, p))

s = "abab"
p = "ab"

print(sol.findAnagrams(s, p))

s = "baa"
p = "aa"

print(sol.findAnagrams(s, p))
