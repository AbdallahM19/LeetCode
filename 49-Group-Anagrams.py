class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(i)
            else:
                anagrams[sorted_word] = [i]
        return list(anagrams.values())