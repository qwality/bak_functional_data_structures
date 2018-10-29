class Stack:
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    def push(self, item):
        return Stack(item, self)

    def push2(self, *items):
        if len(items) is 1:
            return Stack(items[-1], self)
        else:
            return Stack(items[-1], self).push2(*items[:-1])

    def isEmpty(self):
        return self.item is None       # porad nevim jestli item nebo next

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

    def __iter__(self):
        if self.isEmpty():      # porad nevim jestli item nebo next
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
