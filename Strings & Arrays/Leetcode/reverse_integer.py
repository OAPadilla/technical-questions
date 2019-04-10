# Given a 32-bit signed integer, reverse digits of an integer.
#
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        seq = str(x)
        seq_list = list(seq)
        is_neg = False

        if len(seq_list) < 2:
            return x

        if seq_list[0] == '-':
            is_neg = True
            del seq_list[0]

        out = ""
        for i in range(len(seq_list)):
            out += seq_list.pop()

        if out[0] == '0':
            out = out[1:]

        if is_neg:
            out = '-' + out

        result = int(out)

        if result > 2**31 - 1 or result < -2**31:
            return 0

        return result

    def reverse_nostring(self, x):
        result = 0
        z = abs(x)      # z = 123

        while (z != 0):
            pop = z % 10    # pop = 3
            z //= 10        # z = 12

            temp = result * 10 + pop
            result = temp

        if x < 0:
            result = -result

        if result > 2**31 - 1 or result < -2**31:
            return 0

        return result


if __name__ == "__main__":
    int_x = -1230
    print(Solution().reverse(int_x))
    print(Solution().reverse_nostring(int_x))
