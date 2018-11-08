class Stack:
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    def isEmpty(self):
        return self.item is None       # don't know which of checking next or item is better

    def push(self, item):
        return Stack(item, self)

    def push2(self, *items):
        if len(items) is 1:
            return Stack(items[-1], self)
        else:
            return Stack(items[-1], self).push2(*items[:-1])

    def pop(self):
        return self.next

    def reversed(self, tmp=None):
        if tmp is None:
            return Stack().reversed(self)
        elif tmp.isEmpty():
            return self
        elif tmp.next.isEmpty():
            return self.push(tmp.top())
        else:
            return self.push(tmp.top()).reversed(tmp.pop())

    def top(self):
        return self.item

    def __reversed__(self):
        if self.isEmpty():
            return
        else:
            yield from self.next.__reversed__()
            yield self.item

    def __iter__(self):
        if self.isEmpty():
            return
        else:
            yield self.item
            yield from self.next.__iter__()

    def __getitem__(self, key):
        return self.item if key is 0 else self.next[key - 1]

    def __str__(self):
        return "{0!s}".format(list(self))

    def __repr__(self):
        return "{self.__class__.__name__}({self.item!s}, {self.next!r})".format(self=self)


class PseudoStack:  # empty Stack
    def isEmpty(self):
        return True

    def push(self, *items):
        if len(items) is 1:
            return Stack2(items[-1])
        else:
            return Stack2(items[-1]).push(*items[:-1])

    def pop(self):
        return None

    def top(self):
        return None

    def reversed(self):
        return self.__reversed__()

    def __reversed__(self):
        return self

    def __iter__(self):
        yield from ()

    def __getitem__(self, key):
        return None

    def __str__(self):
        return "[]"

    def __repr__(self):
        return "{self.__class__.__name__}(empty)".format(self=self)


class Stack2(PseudoStack):
    def __init__(self, item, _next=PseudoStack()):
        super().__init__()
        self.item = item
        self._next = _next

    @staticmethod
    def empty():
        return PseudoStack()

    def isEmpty(self):
        return False

    def push(self, *items):
        if len(items) is 1:
            return Stack2(items[-1], self)
        else:
            return Stack2(items[-1], self).push(*items[:-1])

    def pop(self):
        return self._next

    def top(self):
        return self.item

    @staticmethod
    def rec_inc_rev(a, b=PseudoStack()):
        if not a.isEmpty():
            return Stack2.rec_inc_rev(a.pop(), b.push(a.top()))
        else:
            return b

    def reversed(self):
        return self.rec_inc_rev(self)

    def __reversed__(self):     # returns true representation or strict iterable
        return self.reversed()
        # try:
        #     yield from self._next.__reversed__()
        # except AttributeError:
        #     pass
        # finally:
        #     yield self.item

    def __iter__(self):
        try:
            yield self.item
            yield from self._next.__iter__()
        except AttributeError:
            return

    def __getitem__(self, key):
        return self.item if key == 0 else self._next[key - 1]

    def __str__(self):
        return "{0}".format(list(self))

    def __repr__(self):
        return "{self.__class__.__name__}({self.item!s}, {self._next.__class__.__name__})".format(self=self)
