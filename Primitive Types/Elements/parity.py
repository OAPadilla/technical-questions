

# Elements 4.1: Parity of a binary word is 1 if the number of 1's in the word is odd; otherwise, it is 0
# Used to check for bit errors in data storage and communication
def parity(x):
    res = 0
    while x:
        res += x & 1
        x >>= 1
    return res

print(parity(10))
