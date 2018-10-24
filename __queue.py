from __stack import Stack


class Queue:
    def __init__(self, incoming=Stack(), outgoing=Stack()):
        self.incoming = incoming
        self.outgoing = outgoing

    def isEmpty(self):
        # presume outgoing is never empty if incoming is not
        return self.outgoing.isEmpty()

    def push(self, item):
        # if both stacks are empty, push outgoing instead
        if self.incoming.isEmpty() and self.outgoing.isEmpty():
            return Queue(
                self.incoming,
                self.outgoing.push(item)
            )
        else:
            return Queue(
                self.incoming.push(item),
                self.outgoing
            )

    def pop(self):
        if not self.isEmpty():
            tmp = Queue(self.incoming, self.outgoing.pop())
            if tmp.isEmpty() and not tmp.incoming.isEmpty():
                # reversing if outgoing is empty and incoming is not
                return Queue(Stack(), tmp.incoming.reversed())
            return tmp
        else:
            return self

    # pops element, if there is none reverse, then return
    # if not self.outgoing.isEmpty():
    # 	return Queue(self.incoming, self.outgoing.pop())
    # elif not self.incoming.isEmpty():
    # 	return Queue(Stack.empty(), self.incoming.reversed().pop())
    # else:
    # 	return self

    def top(self):
        return self.incoming.top()

    def bot(self):
        return self.outgoing.top()

    def __str__(self):
        return "{self.incoming!s}{R!s}".format(R=self.outgoing.reversed(), self=self)

    def __repr__(self):
        return "{self.__class__.__name__}({self.incoming!r}, {self.outgoing!r})".format(self=self)
