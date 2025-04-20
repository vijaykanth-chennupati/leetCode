class Solution(object):
    def reverseString(self, s):
        count = len(s)
        for i in range(count):
             j = count - i - 1
             if i > j:
                return s
             s[i],s[j] = s[j],s[i]
                
        
                
        
        