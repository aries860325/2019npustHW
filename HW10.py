class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(set(nums))
        result =2 * total - sum(nums)
        return result