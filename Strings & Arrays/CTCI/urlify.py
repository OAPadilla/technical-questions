# 1.3 URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can perform this
# operation in place.)

# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

str = "Mr John Smith      "
real_len = 13

def urlify(str, real_len):
    if real_len == 0:
        return ""

    new_str = str.lstrip(' ')[:13]
    new_str = new_str.replace(" ", "%20")

    print(new_str)


urlify(str, real_len)


def urlify2(str, x):
    str = str[:x]
    str = str.split(" ")
    return "%20".join(str)

# num = [4,1,2,3,5,6]
#
# def arrayCheck(nums):
#     for x in range(len(num)-1):
#         if nums[x]==1 and nums[x+1]==2 and nums[x+2]==3:
#             return True
#     return False
#
# print(arrayCheck(num))
