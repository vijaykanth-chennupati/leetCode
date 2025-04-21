class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==1:
            return 1
        k=0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = "_"
            else:
                nums[k],nums[i] = nums[i],nums[k]
                k+=1
        i=i+1
        if i == len(nums)-1:
            nums[k],nums[i] = nums[i],nums[k]
            k+=1
        return k
        