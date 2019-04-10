# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


def max_subarray(nums):
    if not nums:
        return 0

    max_sum = curr_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, max_sum + curr_sum)

    return max_sum

# Java Solution
#
# public int maxSubArray(int[] nums) {
#     int max = Integer.MAX_VALUE;
#     int sum = 0;
#     for (int i = 0; i < nums.length; i++) {
#         if (sum < 0)
#             sum = A[i]
#         else
#             sum += A[i]
#         if (max < sum)
#             max = sum
#     }
#     return max
# }
