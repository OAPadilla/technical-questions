

# 11.1 SEARCH A SORTED ARRAT FOR FIRST OCCURANCE OF K
def search_first_of_k(k, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) / 2
        if A[M] < k:
            U = M - 1
        elif A[M] > k:
            L = M + 1
        else:
            while M >= 0:
                if A[M-1] != k:
                    break
                M -= 1
        return M


def search_first_of_k2(k, A):
    left, right = 0, len(A) - 1
    result = -1
    while left <= right:
        mid = (left - right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result