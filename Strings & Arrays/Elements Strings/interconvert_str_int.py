import functools
import string

# 6.1 INTERCONVERT STRINGS AND INTEGERS
def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) \
                            * (-1 if s[0] == '-' else 1)


print(int_to_string(123))
print(string_to_int('123'))