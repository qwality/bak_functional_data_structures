from __stack import Stack
from __queue import Queue


class Pseudo:
    def __init__(self, _a=Stack(), a_=Stack()):
        self._a = _a
        self.a_ = a_

    def isEmpty(self):
        return self.a_.isEmpty()

    def inc_rev(self):
        return Pseudo(
            self._a.push(self.a_.top()),
            self.a_.pop()
        ) #if not self.isEmpty() else self

    def __str__(self):
        # return self.__repr__()
        return "{self._a!s}{T!s}".format(T=list(self.a_.reversed()), self=self)

    def __repr__(self):
        return "{self.__class__.__name__}({self._a!s}{T!s})".format(T=list(self.a_.reversed()), self=self)


class Queue2(Queue):
    def __init__(self, head=Stack(), tail=Stack(), d=0):
        super().__init__(head, tail)
        self.d = d

    def push(self, item):
        d = self.d - 1
        tmp = Queue2(
            self.head,
            self.tail.push(item),
            d,
        )
        if d >= 0:
            return tmp
        else:
            return Phase1.cons(tmp)

    def r(self):
        return Queue2(
            head=self.tail.reversed(),
            tail=Stack(),
            d=len(list(self.tail))
        )

    def pop(self):
        d = self.d - 1
        tmp = Queue2(
            self.head.pop(),
            self.tail,
            d
        )
        if d >= 0:
            return tmp
        else:
            return Phase1.cons(tmp)

    def __str__(self):
        return "{self.__class__.__name__} H={self.head!s}, T={R!s}, d={self.d}".format(self=self, R=list(self.tail.reversed()))


class Phase1(Queue):
    #                  head, None, 0, head, tail,       None,       None
    def __init__(self, head, tail, h=Pseudo(), t=Pseudo(), d=-1):
        super().__init__(head, tail)
        self.h = h
        self.t = t
        self.d = d

    @staticmethod
    def step(h, t, d):
        if not t.isEmpty():
            if not h.isEmpty():
                return h.inc_rev(), t.inc_rev(), d + 1
            else:
                return h, t.inc_rev(), d + 1
        else:
            return h, t, d

    @staticmethod
    def cons(queue2):
        tmp = Phase1(
            queue2.head,
            Stack(),
            *Phase1.step(
                Pseudo(Stack(), queue2.head),
                Pseudo(Stack(), queue2.tail),
                queue2.d
            )
        )
        if tmp.t.isEmpty():
            return Phase2.cons(Phase1(
                tmp.head,
                tmp.tail,
                *tmp.step(
                    tmp.h,
                    tmp.t,
                    tmp.d
                )
            ))
        else:
            return tmp



    def push(self, item):
        tmp = Phase1(
            self.head,
            self.tail.push(item),
            *self.step(*self.step(
                self.h,
                self.t,
                self.d
            ))
        )

        if not tmp.t.isEmpty():
            return tmp
        else:
            return Phase2.cons(tmp)

    def pop(self):
        tmp = Phase1(
            self.head.pop(),
            self.tail,
            *self.step(*self.step(
                self.h,
                self.t,
                self.d - 1
            ))
        )

        if not tmp.t.isEmpty():
            return tmp
        else:
            return Phase2.cons(tmp)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ("---------------------------\n" +
                "{self.__class__.__name__}" + super().__str__() + "\n" +
                "{self.h} {self.t} {self.d}").format(self=self)


class Phase2(Queue):
    def __init__(self, head, tail, p, d):
        super().__init__(head, tail)
        self.p = p
        self.d = d

    @staticmethod
    def cons(phase1):
        tmp = Phase2(
            phase1.head,
            phase1.tail,
            Pseudo(phase1.t._a, phase1.h._a),
            phase1.d
        )
        if tmp.p.isEmpty():
            return tmp.g()
        else:
            return tmp
        # if not tmp.p.isEmpty():
        #     return tmp
        # else:
        #     "slon"

    @staticmethod
    def step(p, d):
        if not p.isEmpty():
            return p.inc_rev(), d - 1
        else:
            return p, d

    def g(self):
        return Queue2(
            self.p._a,
            self.tail,
            len(list(self.p._a))
        )

    def push(self, item):
        tmp = Phase2(
            self.head,
            self.tail.push(item),
            *self.step(*self.step(
                self.p,
                self.d
            ))
        )
        if self.d == 1:
            return tmp.g()
        else:
            return tmp

    def pop(self):
        d = self.d - 1
        if d <= 0:
            return Phase2(
                self.head.pop(),
                self.tail,
                self.p,
                self.d
            ).g()
        else:
            return Phase2(
                self.head.pop(),
                self.tail,
                *self.step(*self.step(
                    self.p,
                    d
                ))
            )

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ("---------------------------\n" +
                "{self.__class__.__name__}" + super().__str__() + "\n" +
                "{self.p} {self.d}").format(self=self)





