from queue import Queue


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
