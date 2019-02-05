# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}

        for counter, num in enumerate(nums):
            sol = target - num
            if sol in elements:
                return [elements[sol], counter]
            elements[num] = counter

if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
