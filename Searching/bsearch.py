

# Binary Search Algorithm
def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) / 2
        if A[M] > t:
            U = M - 1
        elif A[M] < t:
            L = M + 1
        else:
            return M
    return -1
