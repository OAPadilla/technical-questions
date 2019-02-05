

# 6.5 TEST PALINDROMICITY
def is_palindrome(s):
    alnum = []
    for i in range(len(s)):
        if s[i].isalnum():
            alnum.append(s[i].lower())

    return alnum == alnum[::-1]


def is_palindrome_inplace(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalnum() is False:
            i += 1
        if s[j].isalnum() is False:
            j -= 1
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        elif s[i].isalnum() and s[j].isalnum():
            return False
    return True


print(is_palindrome_inplace("Amore, Roma."))
print(is_palindrome_inplace("A man, a plan, a canal, Panama."))
print(is_palindrome_inplace("Ray a Ray"))
print(is_palindrome_inplace("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a "
                            "man; a prisoner up to new era."))
