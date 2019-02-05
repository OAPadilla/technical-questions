

# 6.4 REPLACE AND REMOVE
def replace_and_remove(size, s):
    # Iterate forward: delete 'b's, count a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # Iterate backwards: replace 'a' with 2 'd's
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
        print(s)
    return (final_size, s)


print(replace_and_remove(7, ['c', 'c', 'd', 'b', 'b', 'c', 'a']))
