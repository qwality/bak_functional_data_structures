class Stack:
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    def push(self, item):
        return Stack(item, self)

    def isEmpty(self):
        return self.item is None       # porad nevim jestli item nebo next

    def pop(self):
        return self.next

    def reversed(self, tmp=None):
        if tmp is None:
            return Stack().reversed(self)
        else:
            return self.push(tmp.top()).reversed(tmp.pop()) if not tmp.next.isEmpty() else self.push(tmp.top())

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
