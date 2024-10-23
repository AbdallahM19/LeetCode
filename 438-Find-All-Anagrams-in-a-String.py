class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        p_len, s_len = len(p), len(s)

        if p_len > s_len:
            return result

        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(p_len):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1

        for i in range(p_len, s_len):
            if p_count == s_count:
                result.append(i - p_len)

            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - p_len]) - ord('a')] -= 1

        if p_count == s_count:
            result.append(s_len - p_len)

        return result