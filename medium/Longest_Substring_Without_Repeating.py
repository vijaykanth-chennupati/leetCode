class Solution(object):
    def lengthOfLongestSubstring(self, s):
        latest={}
        strt=0
        max_len=0
        for i in range(len(s)):
            if s[i] in latest and latest[s[i]]>=strt:
                strt = latest[s[i]]+1
            latest[s[i]]=i
            max_len = max(max_len, i - strt + 1)
        return max_len

"""
        |--------|---|------|--------|


"""