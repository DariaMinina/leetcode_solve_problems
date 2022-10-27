import itertools


class ZigzagIterator:
    def __init__(self, v1, v2):
        def vals():
            for i in itertools.count():
                for v in v1, v2:
                    if i < len(v):
                        yield v[i]
        self.vals = vals()
        self.n = len(v1) + len(v2)

    def hasNext(self):
        return self.n > 0

    def next(self):
        self.n = self.n - 1
        return next(self.vals)


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6, 8, 10]
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
    print(v)




