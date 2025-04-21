class Solution(object):
    def isPalindrome(self, s):
        s1=s.lower()
        i = 0
        j = len(s1)-1
        if (ord(s1[i]) not in range(97,123)) and (ord(s1[i]) not in range(48,58)) and (len(s1)==1):
            return True
        
        while i < j:
            if (ord(s1[i]) in range(97,123)) or (ord(s1[i]) in range(48,58)):
                if (ord(s1[j])  in range(97,123)) or (ord(s1[j]) in range(48,58)):
                    if s1[i] != s1[j]:
                        return False
                    else:
                        i+=1
                        j-=1
                else:
                    j-=1
            else:
                i+=1
        return True