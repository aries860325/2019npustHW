class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = {}
        for i in range(len(nums)):
            if (target - nums[i]) in array:
                return [array[target - nums[i]], i]
            array[nums[i]] = i