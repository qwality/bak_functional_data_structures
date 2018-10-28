from __queue import Queue
from __queue2 import *
from __stack import Stack


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
    # print(Stack().reversed())
    # a = Stack().push2(1, 2, 3)
    # print(a)
    # print(a.pop())
    # print("--Queue--")
    # print(Queue().push(1))
    # print(Queue().push(1).push(2))
    # print(Queue().push(1).push(2).push(3))
    # print(Queue().push(1).push(2).push(3).pop())
    # x = Queue().push(1).push(2).push(3).pop().push(4)
    # print(x)
    # print(repr(x))
    # print(Queue().push(1).push(2).push(3).pop().push(4).pop())
    # print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop())
    # print(Queue().push(1).push(2).push(3).pop().push(4).pop().pop().pop())
    # a = Queue().push(1).push(2).push(3).push(4)
    # b = a.pop()
    # c = b.push(5).push(6).push(7)
    # print(a, b, c, sep='\n')

    print("--Queue 2--")
    a = Queue2()
    b = a.push(1)
    b1 = b.push(2)
    b2 = b1.push(3)
    c = b2.r()
    d = c.pop().push(4)
    print(a, b, b1, c, d, sep="\n")
    # A = Queue2(Stack(1, Stack(None, None)))
    # B = Phase2(A)
    # print(A, B.tail)




if __name__ == "__main__":
    main()
