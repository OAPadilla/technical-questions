# 1.9 String Rotation: Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").


def string_rotation(s1, s2):
    """
    :type s1, s2: str
    :rtype: bool
    """
    lengths1 = len(s1)
    lengths2 = len(s2)

    if (lengths1 == lengths2) and lengths1 > 0:
        s3 = s1 + s1
        return is_substring(s3, s2)

    return False


if __name__ == "__main__":
    print(is_substring(s1,s2))
