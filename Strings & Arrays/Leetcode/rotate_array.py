# Given an array, rotate the array to the right by k steps, where k is non-negative.


def rotate(nums, k):
    if not nums:
        return nums

    n = len(nums) - k
    return nums[n:] + nums[:n]