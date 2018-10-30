from __queue2 import *
from functools import reduce


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


def main():

    # todo iterator for queues, reversed-jen obratit poradi yieldu, __str__ pomoci __iter__

    print("--Stack--")
    # test(Stack(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0])

    print("\n--Pseudo--")
    pseudo = Pseudo(Stack().push2(1, 2, 3), Stack().push2(6, 5, 4))
    print(pseudo, repr(pseudo), sep="\n")

    print("\n--Queue--")
    test(Queue(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], compose(print, str))

    print("\n--Queue 2--")
    test(Queue2(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0], compose(print, repr))
    print("Queue2	[4, 5, 7, 8, 9, 10] [11], d=5")

    print("\n--tests--")
    print(test(
        Queue2(),
        [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        compose(print, repr)
    ))


if __name__ == "__main__":
    main()
