class Solution(object):
    def isPalindrome(self, x):
        back = str(x)[:: - 1 ]
        if(x >= 0 and str(x) == back):
            return True
        else:
            return False