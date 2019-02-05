# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0

    for i in range(len(s)-1):
        val = symbols[s[i]]

        if symbols[s[i]] < symbols[s[i+1]]:
            val = -symbols[s[i]]

        sum += val

    return sum + symbols[s[-1]]


if __name__ == "__main__":
    q = "III"       # 3
    r = "LVIII"     # 58
    s = "MCMXCIV"   # 1994
    t = "IV"        # 4
    u = "IX"        # 9

    print(romanToInt(q))
    print(romanToInt(r))
    print(romanToInt(s))
    print(romanToInt(t))
    print(romanToInt(u))