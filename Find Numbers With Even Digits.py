class Solution(object):
    
    def findNumbers(self, nums):
        m = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        for i in range(len(nums)):
            if len(nums[i]) % 2 == 0:
                m+=1
            else:
                continue
        return m
            
