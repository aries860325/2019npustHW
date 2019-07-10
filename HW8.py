class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sp = s.split()
        le = len(s.split())
        if le != 0:
            return len(s.split()[le-1])
        else:
            return le