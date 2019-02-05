

# 8.3 TEST A STRING OVER "{,},(,),[,]" FOR WELL-FORMEDNESS
def is_well_formed(s):

    stack = []
    lookup = {"{": "}", "[": "]", "(": ")"}

    for c in s:
        if c in lookup:
            stack.append(c)
        elif len(stack) == 0 or lookup[stack.pop()] != c:
            return False

    if len(stack) != 0:
        return False

    return True

print(is_well_formed("[[{()()}{()}]()"))
