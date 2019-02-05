# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def is_one_away(str1, str2):
    """
    :type str1: string
    :type str2: string
    :rtype: bool
    """
    len1 = len(str1)
    len2 = len(str2)

    if abs(len1 - len2) > 1:
        return False

    # Number of edits
    edits = 0

    # Position in string
    pos1 = 0
    pos2 = 0

    while len1 > pos1 and len2 > pos2:
        # If current characters don't match
        if str1[pos1] != str2[pos2]:
            edits += 1
            # If edit counter greater than 1 return false
            if edits > 1:
                return False
            # If len of one string greater, move its position forward
            if len1 > len2:
                pos1 += 1
            elif len1 < len2:
                pos2 += 1
            # Else if same lengths move both positions
            else:
                pos1 += 1
                pos2 += 1
        # Else, move ahead in both strings
        else:
            pos1 += 1
            pos2 += 1

    return True


if __name__ == "__main__":
    a1, a2 = ("pale", "ple")    # true
    b1, b2 = ("pales", "pale")  # true
    c1, c2 = ("pale", "bale")   # true
    d1, d2 = ("pale", "bake")   # false

    print(is_one_away(a1, a2))
    print(is_one_away(b1, b2))
    print(is_one_away(c1, c2))
    print(is_one_away(d1, d2))
