class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            elif nums[i] >= target:
                return i
        return i+1
        
