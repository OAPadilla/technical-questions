

# 5.2
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 0
        A.insert(0, 1)

    return A


print(plus_one([1, 2, 9]))
