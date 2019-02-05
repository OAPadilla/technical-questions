# 3.3 Stack of Plates:
# Imagine a  stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).

class Stack:

    def __init__(self, capacity):
        self.
        self.capacity = capacity

class SetOfStacks:

    def __init__(self, capacity, next_stack=None):
        self.capacity = capacity
        self.stack = []

    def push(self, x):
        if len(self.elements) == self.threshold:
            SetOfStacks(10).elements.append(x)
        else:
            self.elements.append(x)
