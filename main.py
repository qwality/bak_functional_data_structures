from __queue2 import *


def test(tst, fnc, lst):
    prev = tst
    for i in lst:
        if i != 0:
            prev = prev.push(i)
            print(fnc(prev))
        else:
            prev = prev.pop()
            print(fnc(prev))

    return prev


def main():

    print("--Stack--")
    # test(Stack(), [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0])

    print("\n--Pseudo--")
    pseudo = Pseudo(Stack().push2(1, 2, 3), Stack().push2(6, 5, 4))
    print(pseudo, repr(pseudo), sep="\n")

    print("\n--Queue--")
    test(Queue(), str, [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0])

    print("\n--Queue 2--")
    test(Queue2(), repr, [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 0])
    print("Queue2	[4, 5, 7, 8, 9, 10] [11], d=5")

    print("\n--tests--")
    print(test(Queue2(), repr, [1, 2, 3, 0, 0, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))





if __name__ == "__main__":
    main()
