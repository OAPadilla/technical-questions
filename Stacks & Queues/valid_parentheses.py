# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, x):
        self.stack.append(x)

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        x = self.stack[-1]
        del self.stack[-1]
        return x


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}

    if len(s) == 1:
        return False

    for c in s:
        if c in mapping:
            if stack.peek() == mapping[c]:
                stack.pop()
            else:
                return False
        else:
            stack.push(c)

    return stack.is_empty()
