# 1.2 Check Permutation:
# Given two strings, write a method to decide if one is a permutation of the other.

# permutations of abc are [abc, acb, bac, bca, cab, cba]

s1 = 'abc'
s2 = 'bac'
s3 = 'ba'


def check_permutation(str1, str2):
    # Permutations must be same length
    if len(str1) != len(str2):
        return False

    # Sort both strings, and then compare
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2

def check_perm(s1, s2):
    if len(s1) != len(s2):
        return False
    my_dict = {}
    for i in s1:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for i in s2:
        if i in my_dict:
            my_dict[i] -= 1
        else:
            my_dict[i] = 1
    for v in my_dict.values():
        if v > 0:
            return False

    return True


# A more efficient algorithm would be to use counters
#print(check_permutation(s1, s2))
print(check_perm(s1,s3))
