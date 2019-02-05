

# 5.1
def dutch_flag_partition(A, i):
    pivot = A[i]

    smaller = 0
    larger = len(A) - 1

    for i in range(len(A)):
        if A[i] < pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1

    return A

print(dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 3))
