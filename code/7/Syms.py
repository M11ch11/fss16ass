import math


class Sym:
    def __init__(i):
        i.counts, i.most, i.mode, i.n = {}, 0, None, 0

    def add(i, x):
        i.n += 1
        new = i.counts[x] = i.counts.get(x, 0) + 1
        if new > i.most:
            i.most, i.mode = new, x
        return x

    def sub(i, x):
        i.n -= 1
        i.counts[x] -= 1
        if x == i.mode:
            i.most, i.mode = None, None

    def ent(i):
        tmp = 0
        for val in i.counts.values():
            p = val / i.n
            if p:
                tmp -= p * math.log(p, 2)
        return tmp

    def show(self):
        return "counts " + str(self.counts) + "\nmost " + str(self.most) + "\nmode " + str(self.mode) + "\nn " + str(
            self.n)

    def norm(i, x):
        return x

    def dist(i, x, y):
        return 0 if x == y else 1

    def furthest(i, x):
        return "SoMEcrazyTHing"