class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        num = x[::-1]
        if x == num:
            return True
        else:
            return False
