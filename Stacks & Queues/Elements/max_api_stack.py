

# 8.1 IMPLEMENT A STACK WITH MAX API
class Stack:

    class MaxWithCount:

        def __init__(self, max, count):
            self.max = max
            self.count = count

    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1] == 0:
                self._cached_max_with_count.pop()
        return pop_element

    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))

