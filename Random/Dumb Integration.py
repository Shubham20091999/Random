# Divide And Concqure
# Bad if at some point value goes to infinity
# import math


class Integration:
    def __init__(self, fn, error=0.01) -> None:
        self.fn = fn
        self.err = error

    def __helper_do(self, l, r, lv, rv):
        m = (l+r)/2
        mv = self.fn(m)
        theo = (lv+rv)/2
        if(abs(mv-theo)/mv < self.err):
            return (r-l)*theo
        return self.__helper_do(l, m, lv, mv)+self.__helper_do(m, r, mv, rv)

    def do(self, l, r):
        lv = self.fn(l)
        rv = self.fn(r)
        return self.__helper_do(l, r, lv, rv)


# Example


# def fn(x):
#     return math.sin(math.cos(x)+math.tan(x)*math.log10(x))


# print(Integration(fn, 0.0000001).do(0.0000000001, math.pi/2))
