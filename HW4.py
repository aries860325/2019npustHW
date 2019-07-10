dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        before = ""
        total  = 0
        for i in s:
            if   before + i == "CM":
                 total += 800
            elif before + i == "CD":
                 total += 300
            elif before + i == "XL":
                 total += 30
            elif before + i == "XC":
                 total += 80
            elif before + i == "IV":
                 total += 3
            elif before + i == "IX":
                 total += 8
            else:
                total += dictionary[i] 
            before = i
        return total