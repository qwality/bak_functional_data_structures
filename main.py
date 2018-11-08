from __queue import *
from functools import reduce
from __stack import *


def compose(*args):
    return reduce(lambda y, x: lambda z: x(y(z)), reversed(args))


def test(tst, lst, fnc=lambda x: x):
    prev = tst
    for i in lst:
        if i != 0:
            prev = prev.push(i)
            fnc(prev)
        else:
            prev = prev.pop()
            fnc(prev)

    return prev


# serves testing purposes
def main():
    # pass
    # print("--Stack--")
    # a = test(Stack2(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0])
    # b = list(reversed(a))
    #
    # # a = Stack2.empty().push(0,1,2,3,4,5,6,7,8,9,10)
    # # b = list(reversed(a))
    # print(a, b, a.reversed(), sep="\n")
    # print(test(Stack(), [1, 2, 3, 0, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], print))
    # print(test(Stack2.empty(), [1, 2, 3, 0, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], print))

    # c = Stack2(0, Stack2(1, Stack2(2, None)))

    # for i in c:
    #     print(i.item)
    #
    # for i in reversed(c):
    #     print(i.item)

    print("\n--Pseudo--")
    pseudo = Pseudo(Stack().push2(1, 2, 3), Stack().push2(6, 5, 4))
    print(pseudo, repr(pseudo), sep="\n")

    print("\n--Queue--")
    test(Queue(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], compose(print, str))
    print("[4, 5, 7, 8, 9, 10, 11]")
    #
    print("\n--Queue 2--")
    test(Queue2(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], compose(print, repr))
    print("Queue2	[4, 5, 7, 8, 9, 10] [11], d=5")

    print("\n--tests--")
    print("\nstr:\t%s" % test(
        Queue2(),
        [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        compose(print, repr)
    ))
    print("ref:\t[3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]")

    for i in Stack2(0):
        print(i)


if __name__ == "__main__":
    main()
