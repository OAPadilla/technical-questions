

# 6.6 REVERSE ALL THE WORDS IN A SENTENCE
def trim_front(words):
    cut = 0
    for w in words:
        if w != '':
            break
        cut += 1
    return words[cut:]


def trim_back(words):
    cut = len(words)
    for w in reversed(words):
        if w != '':
            break
        cut -= 1
    return words[:cut]


def reverse_words(s):
    if len(s) == 0:
        return ''
    if len(s) == 1 and s[0] == ' ':
        return ''

    words = s.split(' ')
    words = trim_front(words)
    words = trim_back(words)

    for w in reversed(range(len(words))):
        if words[w] == '':
            del words[w]

    return ' '.join(words[::-1])


print(reverse_words("Alice likes Bob a lot"))
print(reverse_words(""))
print(reverse_words(" "))
print(reverse_words(" Alice likes Bob a lot"))
print(reverse_words("Alice  likes   Bob    a lot    "))
