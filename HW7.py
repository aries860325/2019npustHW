class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = 0
        for i in range(0 , len(nums)):
            if(nums[i] == target):
                return i
            elif(nums[i] != target and n == 0):
                n = n + 1
                nums.append(target)
                nums.sort()
                return nums.index(target)
