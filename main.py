class Stack:
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    def push(self, item):
        return Stack(item, self)

    def isEmpty(self):
            return self.item is None       #  porad nevim jestli item nebo next

    def pop(self):
        return self.next

    def reversed2(self, tmp=None):
        if tmp is None:
            return Stack().reversed2(self)
        else:
            return self.push(tmp.top()).reversed2(tmp.pop()) if not tmp.next.isEmpty() else self.push(tmp.top())

    def r(self, tmp):
        return self.push(tmp.top()).r(tmp.pop()) if not tmp.next.isEmpty() else self.push(tmp.top())

    def reversed(self):
        return Stack().r(self)

    reversed = reversed2

    def top(self):
        return self.item

    def __iter__(self):
        if self.isEmpty():      #  porad nevim jestli item nebo next
            return
        else:
            yield self
            yield from self.next.__iter__()

    def __getitem__(self, key):
        return self.item if key is 0 else self.next[key - 1]

    def __str__(self):
        return str(list(map(lambda x: x.item, self)))


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
        return str(self.incoming) + str(self.outgoing)


def main():
    # print("--reversed test--")
    # b = Stack.empty().push(1).push(2).push(3).push(4)
    # print(b)
    # c = b.reversed()
    # print(c)
    # print("--Queue test--")
    # a = Queue.empty()
    # print("empty: ", a)
    # b = a.push(1)
    # c = b.push(2)
    # print("push(1), push(2): ", b, ",",  c)
    # d = c.pop()
    # print(Queue.empty().push(1))
    # print(Queue.empty().push(1).pop())
    print("--final test--")
    print(Queue().push(1))
    print(Queue().push(1).push(2))
    print(Queue().push(1).push(2).push(3))
    print(Queue().push(1).push(2).push(3).pop())
    x = Queue().push(1).push(2).push(3).pop().push(4)
    print(x)
    print(x)
    print(Queue().push(1).push(2).push(3).pop().push(4).pop())
    print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop())
    print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop().pop())
    # nejaky srandovni komentar
    # dalsi srandovni komentar


if __name__ == "__main__":
    main()
