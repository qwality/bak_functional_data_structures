from __stack import Stack


class Queue:
    def __init__(self, tail=Stack(), head=Stack()):
        self.tail = tail
        self.head = head

    def isEmpty(self):
        # presume head is never empty if tail is not
        return self.head.isEmpty()

    def push(self, item):
        # if both stacks are empty, push head instead
        if self.tail.isEmpty() and self.head.isEmpty():
            return Queue(
                self.tail,
                self.head.push(item)
            )
        else:
            return Queue(
                self.tail.push(item),
                self.head
            )

    def pop(self):
        if not self.isEmpty():
            tmp = Queue(self.tail, self.head.pop())
            if tmp.isEmpty() and not tmp.tail.isEmpty():
                # reversing if head is empty and tail is not
                return Queue(Stack(), tmp.tail.reversed())
            return tmp
        else:
            return self

    # pops element, if there is none reverse, then return
    # if not self.head.isEmpty():
    # 	return Queue(self.tail, self.head.pop())
    # elif not self.tail.isEmpty():
    # 	return Queue(Stack.empty(), self.tail.reversed().pop())
    # else:
    # 	return self

    def top(self):
        return self.tail.top()

    def bot(self):
        return self.head.top()

    def __str__(self):
        return "{self.head!s}{R!s}".format(R=list(self.tail.reversed()), self=self)

    def __repr__(self):
        return "{self.__class__.__name__}({self.head!r}, {self.tail!r})".format(self=self)
