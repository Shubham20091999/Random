# Divide And Concqure
import math


class Integration:
    def __init__(self, fn, error=0.01) -> None:
        self.fn = fn
        self.err = error

    def __helper_do(self, l, r, lv, rv):
        m = (l+r)/2
        mv = self.fn(m)
        if(abs(mv-(lv+rv)/2)/mv*100 < self.err):
            return (r-l)*mv
        return self.__helper_do(l, m, lv, mv)+self.__helper_do(m, r, mv, rv)

    def do(self, l, r):
        lv = self.fn(l)
        rv = self.fn(r)
        return self.__helper_do(l, r, lv, rv)

# Example


# def fn(x):
#     return math.sin(x)*math.cos(x)/100


# print(Integration(fn, 0.0001).do(0, math.pi/2))
