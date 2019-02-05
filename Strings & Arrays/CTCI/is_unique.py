# 1.1 Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# O(n)

str1 = 'abcddef'
str2 = 'abcdef'
str3 = ''


def is_unique(s):
    # Assuming character set is ASCII (128 characters)
    if len(s) > 128:
        return False

    # Fill an array of bool 'False' for all 128 characters
    char_set = [False for _ in range(128)]

    for c in s:
        val = ord(c)        # Assigns ascii deci to 'val'
        if char_set[val]:   # If 'val' location in array is true
            return False    # then its not unique
        else:               # Else, char is unique and the bool is turned True in the array
            char_set[val] = True

    return True

print(is_unique(str1))
print(is_unique(str2))
print(is_unique(str3))
