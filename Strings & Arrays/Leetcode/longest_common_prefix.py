# Write a function to find the longest common prefix string amongst an array of strings.
# All given inputs are in lowercase letters a-z.
# If there is no common prefix, return an empty string "".


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    pos = 0
    out = ""

    if len(strs) == 0:
        return out

    if len(strs) == 1:
        return strs[0]

    # Find shortest length string in List
    minimum = min(strs, key=len)
    # Compare strings using indexes one position at a time
    # If there's more than one string to compare to
    while pos < len(minimum):
        for word in strs:
            if word[pos] != strs[0][pos]:
                return out
        out += strs[0][pos]
        pos += 1

    return out

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]

    print(longest_common_prefix(strs1))
    print(longest_common_prefix(strs2))
