class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                m += 1
            if nums[i] != 1:
                m = 0
            if m > max:
                max = m
            
        return max
