from __stack import Stack
from __queue import Queue


class Queue2(Queue):
    def __init__(self, head=Stack(), tail=Stack(), d=0):
        super().__init__(head, tail)
        self.d = d

    def push(self, item):
        tmp = self.tail.push(item)
        d = self.d - 1
        if d >= 0:
            return Queue2(
                self.head,
                tmp,
                d,
            )
        else:
            return Phase1(
                self.head,
                Stack(),
                0,
                self.head,
                tmp
            )

    def r(self):
        return Queue2(
            head=self.tail.reversed(),
            tail=Stack(),
            d=len(list(self.tail))
        )

    def pop(self):
        tmp = self.head.pop()
        d = self.d - 1
        if d >= 0:
            return Queue2(
                tmp,
                self.tail,
                d
            )
        else:
            return Phase1(
                tmp,
                Stack(),
                0,
                tmp,
                self.tail
            )

    def __str__(self):
        return "{self.__class__.__name__} H={self.head!s}, T={R!s}, d={self.d}".format(self=self, R=list(self.tail.reversed()))


class Phase1(Queue2):
    #                  head, None, 0, head, tail,       None,       None
    def __init__(self, head, tail, d,   _h,   _t, h_=Stack(), t_=Stack()):
        super().__init__(head, tail, d)
        self._h = _h
        self._t = _t
        self.h_ = h_
        self.t_ = t_

    # @staticmethod
    # def inc_rev(_a, a_):
    #

    def step(self):
        return Phase1(
            self.head,
            self.tail,
            self.d,
            self._h,
            self._t,
            self.h_,
            self.t_
        )


    def push(self, item):
        return Phase1(
            self.head,
            self.tail,
            self.d,
            self._h,
            self._t.push(item),
            self.h_,
            self.t_
        )


class Phase2(Queue2):
    pass
