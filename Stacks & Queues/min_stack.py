# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return "Stack is empty"
        x = self.stack[-1]
        del self.stack[-1]
        return x

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

    def get_min(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return "Stack is empty"
        return min(self.stack)


if __name__ == '__main__':
    minStack = MinStack()       # Initiate Stack
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack)             # --> Returns [-2, 0, -3]

    print(minStack.get_min())   # --> Returns -3
    minStack.pop()
    print(minStack.top())       # --> Returns 0
    print(minStack.get_min())   # --> Returns -2

    print(minStack)             # --> Returns [-2, 0]
