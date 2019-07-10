class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if((needle in haystack) == True):
            result = haystack.index(needle)
            return result
        else:
            return -1