class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dic = {}
        start = 0
        for i, char in enumerate(s):
            if char in dic:
                res = max(res, i - start)
                start = max(dic[char] + 1, start)
            dic[char] = i
        return max(res, len(s) - start)







