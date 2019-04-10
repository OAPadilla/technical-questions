# Given an array nums, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.


def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums


print(move_zeroes([0, 1, 0, 3, 12]))