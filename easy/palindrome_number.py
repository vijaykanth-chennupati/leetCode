class Solution(object):
    def isPalindrome(self, x):
        x1 = x
        previous = 0
        while True:
            element = x1 % 10
            previous = (previous * 10) + element
            x1 = x1 // 10
            if x1 == -1:
                return False
            if x1 == 0:
                if x == previous:
                    return True
                else:
                    return False