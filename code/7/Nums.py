import math

def max(x, y): return x if x > y else y


def min(x, y): return x if x < y else y


class Num:
    def __init__(i):
        i.mu, i.n, i.m2, i.up, i.lo = 0, 0, 0, -10e32, 10e32

    def add(i, x):
        i.n += 1
        x = float(x)
        if x > i.up: i.up = x
        if x < i.lo: i.lo = x
        delta = x - i.mu
        i.mu += delta / i.n
        i.m2 += delta * (x - i.mu)
        return x

    def sub(i, x):
        i.n = max(0, i.n - 1)
        delta = x - i.mu
        i.mu = max(0, i.mu - delta / i.n)
        i.m2 = max(0, i.m2 - delta * (x - i.mu))

    def sd(i):
        return 0 if i.n <= 2 else (i.m2 / (i.n - 1)) ** 0.5

    def show(self):
        return "mu " + str(self.mu) + "\nn " + str(self.n) + "\nm2 " + str(self.m2) + "\nup " + str(
            self.up) + "\nlo " + str(self.lo)

    def norm(i, x):
        tmp = (x - i.lo) / (i.up - i.lo + 10 ** -32)
        if tmp > 1:
            return 1
        elif tmp < 0:
            return 0
        else:
            return tmp

    def dist(i, x, y):
        return i.norm(x) - i.norm(y)

    def furthest(i, x):
        return i.up if x < (i.up - i.lo) / 2 else i.lo

    def equalWidthDiscret(self, countBins, value):
        sizeOneBin = (self.up - self.lo) / countBins
        '''create bins'''
        for i in range(0,countBins):
            self.bin[i]=(i*sizeOneBin, (i+1)*sizeOneBin-1)
        return self.bin[value // sizeOneBin]

    def equalFreqDiscret(self, countBins, value):
        self.values = sorted(self.values)
        countPerBin = values.n // countBins
        countValuesSmaller = 0
        n = 0
        while (i < value):
            i = values(n++)
            countValuesSmaller++
        countBinsSmaller = math.ceil(countValuesSmaller / countPerBin)
        return self.bin[countBinsSmaller]
            
