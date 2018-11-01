from __stack import *
# from __queue import Queue

stack = Stack2.empty()


class Pseudo:
    def __init__(self, head=stack, tail=stack):
        self.head = head
        self.tail = tail

    @staticmethod
    def empty_stack():
        return stack

    def isEmpty(self):
        return self.tail.isEmpty()

    def inc_rev(self):
        return Pseudo(
            self.head.push(self.tail.top()),
            self.tail.pop()
        )

    def __str__(self):
        return "[{H}{sep}{T}]".format(
            T=", ".join(map(str, reversed(self.tail))),
            H=", ".join(map(str, iter(self.head))),
            sep=", " if not self.tail.isEmpty() else ""
        )

    def __repr__(self, class_name=True):
        return "{class_name}\t{self.head!s} {T!s}".format(
            class_name=self.__class__.__name__ if class_name else "",
            T=list(reversed(self.tail)),
            self=self
        )


class Queue(Pseudo):
    def __init__(self, head=Pseudo.empty_stack(), tail=Pseudo.empty_stack()):
        super().__init__(head, tail)

    def isEmpty(self):
        return self.head.isEmpty()

    def push(self, item):
        if self.tail.isEmpty() and self.head.isEmpty():
            return Queue(
                self.head.push(item),
                self.tail
            )
        else:
            return Queue(
                self.head,
                self.tail.push(item)
            )

    def pop(self):
        if not self.isEmpty():
            tmp = Queue(self.head.pop(), self.tail)
            if tmp.isEmpty() and not tmp.tail.isEmpty():
                return Queue(tmp.tail.reversed(), Pseudo.empty_stack())
            return tmp
        else:
            return self

    def top(self):
        return self.tail.top()

    def bot(self):
        return self.head.top()


class Queue2(Queue):
    def __init__(self, head=Pseudo.empty_stack(), tail=Pseudo.empty_stack(), d=0):
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

    def __repr__(self, class_name=True):
        return "{super}, d={self.d}".format(
            super=super().__repr__(class_name),
            self=self
        )


class Phase1(Queue2):
    def __init__(self, head, tail, d, h, t):
        super().__init__(head, tail, d)
        self.h = h
        self.t = t

    @staticmethod
    def step(d, h, t):
        if not t.isEmpty():
            if not h.isEmpty():
                return d + 1, h.inc_rev(), t.inc_rev()
            else:
                return d + 1, h, t.inc_rev()
        else:
            return d, h, t

    @staticmethod
    def cons(queue2):
        tmp = Phase1(
            queue2.head,
            Stack(),
            *Phase1.step(*Phase1.step(
                queue2.d,
                Pseudo(Pseudo.empty_stack(), queue2.head),
                Pseudo(Pseudo.empty_stack(), queue2.tail)
            ))
        )
        if not tmp.t.isEmpty():
            return tmp
        else:
            return Phase2.cons(tmp)

    def push(self, item):
        tmp = Phase1(
            self.head,
            self.tail.push(item),
            *self.step(*self.step(
                self.d,
                self.h,
                self.t
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
                self.d - 1,
                self.h,
                self.t
            ))
        )

        if not tmp.t.isEmpty():
            return tmp
        else:
            return Phase2.cons(tmp)

    def __str__(self):
        return "[{head}{0}{t}{1}{h}{2}{tail}]".format(
            ", " if not self.t.tail.isEmpty() else "",
            ", " if not self.t.head.isEmpty() else "",
            ", " if not self.tail.isEmpty() else "",
            head=", ".join(map(str, iter(self.head))),
            t=", ".join(map(str, reversed(self.t.tail))),
            h=", ".join(map(str, iter(self.t.head))),
            tail=", ".join(map(str, reversed(self.tail)))
        )

    def __repr__(self, class_name=True):
        return "{super}\n\t{H} {T}".format(
            super=super().__repr__(),
            H=self.h.__repr__(False),
            T=self.t.__repr__(False),
            self=self
        )


class Phase2(Queue2):
    def __init__(self, head, tail, d, p):
        super().__init__(head, tail, d)
        self.p = p

    @staticmethod
    def step(d, p):
        if not p.isEmpty() and d > 0:
            return d - 1, p.inc_rev()
        else:
            return d, p

    @staticmethod
    def cons(phase1):
        tmp = Phase2(
            phase1.head,
            phase1.tail,
            *Phase2.step(*Phase2.step(
                phase1.d,
                Pseudo(phase1.t.head, phase1.h.head)
            ))
        )
        if tmp.d == 0:
            return tmp.g()
        else:
            return tmp

    def g(self):
        return Queue2(
            self.p.head,
            self.tail,
            len(list(self.p.head)) - len(list(self.tail))
        )

    def push(self, item):
        tmp = Phase2(
            self.head,
            self.tail.push(item),
            *self.step(*self.step(
                self.d,
                self.p
            ))
        )
        if tmp.d == 0:
            return tmp.g()
        else:
            return tmp

    def pop(self):
        tmp = Phase2(
            self.head.pop(),
            self.tail,
            *self.step(*self.step(
                self.d - 1,
                self.p
            ))
        )
        if tmp.d == 0:
            return tmp.g()
        else:
            return tmp

    def __str__(self):
        return "[{t}{0}{h}{1}{T}]".format(
            ", " if not self.p.tail.isEmpty() else "",
            ", " if not self.tail.isEmpty() else "",
            t=", ".join(map(str, reversed(list(iter(self.p.tail))[:self.d]))),
            h=", ".join(map(str, iter(self.p.head))),
            T=", ".join(map(str, reversed(self.tail)))
        )

    def __repr__(self, class_name=True):
        return "{super}\n\t{P}".format(
            super=super().__repr__(),
            P=self.p.__repr__(False),
            self=self
        )





