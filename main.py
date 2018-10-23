class Stack:
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    def push(self, item):
        return Stack(item, self)

    def isEmpty(self):
        return self.item is None

    def pop(self):
        return self.next

    def r(self, tmp):
        return self.push(tmp.top()).r(tmp.pop()) if not tmp.next.isEmpty() else self.push(tmp.top())

    def reversed(self):
        return Stack().r(self)

    def top(self):
        return self.item

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current.item is None:
            raise StopIteration
        else:
            tmp = self.current
            self.current = self.current.next
            return tmp

    def __getitem__(self, key):
        return self.item if key is 0 else self.next[key - 1]

    def __str__(self):
        return str(list(map(lambda x: x.item, self)))


class Queue:
    def __init__(self, incoming=Stack(), outgoing=Stack()):
        self.incoming = incoming
        self.outgoing = outgoing

    # @staticmethod
    # def empty():
    # 	return Queue(Stack(), Stack())

    def isEmpty(self):
        # presume outgoing is never empty if incoming is not
        return self.outgoing.isEmpty()

    def push(self, item):
        # if both stacks are empty, push outgoing instead
        return Queue(self.incoming,
                     self.outgoing.push(item)) if self.incoming.isEmpty() and self.outgoing.isEmpty() else Queue(
            self.incoming.push(item), self.outgoing)

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
    print(Queue().push(1).push(2).push(3).pop().push(4))
    print(Queue().push(1).push(2).push(3).pop().push(4).pop())
    print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop())
    print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop().pop())
    # nejaky srandovni komentar
    # dalsi srandovni komentar


if __name__ == "__main__":
    main()
