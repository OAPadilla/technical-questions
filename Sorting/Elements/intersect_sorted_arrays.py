

# 13.1 COMPUTE THE INTERSECTION OF TWO SORTED ARRAYS

# Brute-force
def intersect_sorted_arrays(a, b):
    i = j = 0
    intersection = []
    while i < len(a) and j < len(b):
        # if matched
        if a[i] == b[j]:
            # check it isn't a duplicate, since arrays are sorted
            if i == 0 or a[i] != a[i-1]:
                intersection.append(a[i])
            i += 1
            j += 1
        # if current element in 'a' is less than 'b', move index in 'a' forward
        elif a[i] < b[j]:
            i += 1
        # else move index in 'b' forward since its less than element in 'a'
        else:       # a[i] > b[j]
            j += 1
    return intersection
