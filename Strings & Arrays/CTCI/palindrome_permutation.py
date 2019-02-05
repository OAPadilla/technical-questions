# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# Count the letters, at most 1 char can have an odd count

def count_char(str):
    """
    :type str: string
    :rtype: hashtable
    """
    char_dict = {}  # letter : counter

    for letter in str.lower():
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    del char_dict[' ']

    return char_dict

def is_palindrome_perm(str):
    """
    :type str: string
    :rtype: bool
    """
    char_dict = count_char(str)

    num_of_oddcount_chars = 0
    for i in char_dict:
        if char_dict[i] % 2 != 0:
            num_of_oddcount_chars += 1
        if num_of_oddcount_chars > 1:
            return False

    return True


if __name__ == "__main__":
    true_input = "Tact Coa"
    false_input = "This isn't a palindrome permutation"
    
    print(is_palindrome_perm(true_input))
    print(is_palindrome_perm(false_input))
