# Given a string, find the length of the longest substring without repeating characters.


# O(n^2) solution: naive
def length_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    curr_len = 0
    pos = 0
    n = len(s)

    while pos < n and curr_len < 95:
        letters = {}
        curr_len = 0
        for i in range(pos, n):
            if s[i] in letters:
                break
            letters[s[i]] = 1
            curr_len += 1
        max_len = max(max_len, curr_len)
        pos += 1

    return max_len


# O(n) solution: "Sliding Window" technique
def length_longest_substring2(s):
    n = len(s)
    letters = {}
    max_len = 0
    i = j = 0

    while i < n and j < n:
        if s[j] not in letters:
            letters[s[j]] = 1
            j += 1
            max_len = max(max_len, j - i)
        else:
            del letters[s[i]]
            i += 1

    return max_len


print(length_longest_substring2("pwwkew"))
print(length_longest_substring2("bbbbb"))
