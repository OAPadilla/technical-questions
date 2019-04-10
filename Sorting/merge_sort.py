

# Merge Sort Algorithm O(n log n)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2     # Find middle element of array
        L = arr[:mid]           # Divide the array to 2 halves
        R = arr[mid:]

        merge_sort(L)           # Sort first half
        merge_sort(R)           # Sort second half

        i = j = k = 0

        # Copy data to temp arrays L & R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
