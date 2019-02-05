# Write a function to find the longest common prefix string amongst an array of strings.
# All given inputs are in lowercase letters a-z.
# If there is no common prefix, return an empty string "".

def is_common_prefix(strs, length):
    pass




def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # Find shortest length string in List
    # Compare strings using indexes one position at a time

    out = ""

    # If there's more than one string to compare to
    if len(strs) > 1:
        shortest = len(strs[0])
        for i in strs:
            if len(strs[i]) < shortest:
                shortest = len(strs[i])



    return out

if __name__ == "__main__":
    strs1 = ["flower","flow","flight"]   # "fl"
    strs2 = ["dog","racecar","car"]     # ""

    print(longestCommonPrefix(strs1))
    print(longestCommonPrefix(strs2))
