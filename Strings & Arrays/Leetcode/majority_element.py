# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.


def majority_element(nums):
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    max_key = None
    for k, v in nums.items():
        if max_key is None or v > count[max_key]:
            max_key = k
    return max_key

