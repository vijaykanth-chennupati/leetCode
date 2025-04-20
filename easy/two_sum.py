class Solution(object):
    def twoSum(self, nums, target):

        array= nums
        result= target
        comp= {}

        for i in range(len(array)):
            diff = result - array[i]
            if diff in comp:
                return [i,comp[diff]]
            else:
                comp[array[i]]= i