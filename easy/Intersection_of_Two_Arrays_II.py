from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = Counter(nums1)
        result = []

        for num in nums2:

            #only if it has anything left to remove kind a balance left
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result