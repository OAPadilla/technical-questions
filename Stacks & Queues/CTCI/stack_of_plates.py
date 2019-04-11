# 3.3 Stack of Plates:

# Imagine a  stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
# and should create a new stack once the previous one exceeds capacity.

# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).


class SetOfStacks:

    def __init__(self, capacity_per_stack):
        self.capacity = capacity_per_stack
        self.stack_of_stacks = [Stack(capacity_per_stack)]

    def __repr__(self):
        return str(self.stack_of_stacks)

    def is_empty(self):
        return len(self.stack_of_stacks) == 0

    # Adds new stack to set of stacks
    def add_stack(self):
        self.stack_of_stacks.append(Stack(self.capacity))

    # Remove empty stacks from set of stacks
    def remove_top_stack(self):
        if self.is_empty():
            return "Set of stacks are empty"
        del self.stack_of_stacks[-1]

    # Pushes to top stack, if stack is full/empty makes new stack and push to that
    def push(self, x):
        if self.stack_of_stacks[-1].is_full() or self.is_empty():
            self.add_stack()
        self.stack_of_stacks[-1].push(x)

    # Returns top element in top stack. If top stack is empty, delete it and return next element on top
    def pop(self):
        if self.stack_of_stacks[-1].is_empty():
            self.remove_top_stack()
        x = self.stack_of_stacks[-1].pop()
        return x


class Stack:

    def __init__(self, capacity_per_stack):
        self.capacity = capacity_per_stack
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, x):
        if self.is_full():
            return "Stack is full"
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        x = self.stack[-1]
        del self.stack[-1]
        return x

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]


if __name__ == '__main__':
    dishes = SetOfStacks(3)
    dishes.push(1)
    dishes.push(2)
    dishes.push(3)
    dishes.push(4)
    dishes.push(5)
    print(dishes)
    dishes.pop()
    print(dishes)
    dishes.pop()
    print(dishes)
    dishes.pop()
    print(dishes)
