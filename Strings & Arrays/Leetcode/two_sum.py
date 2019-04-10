# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# Returns the two indices
def two_sum(nums, target):
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


# Returns the two numbers in a set of unqiue numbers
def two_sum2(nums, target):
    elements = {}
    for n in nums:
        sol = target - n
        elements[sol] = n

    for s in nums:
        if s in elements and s != elements[s]:
            return [elements[s], s]


if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))
