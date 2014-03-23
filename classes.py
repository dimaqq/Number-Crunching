#!/usr/bin/env python
import data


class Point(object):
    def __init__(self, r, x):
        self.r = r
        self.x = x

    def next(self):
        self.x = self.r * self.x * (1 - self.x)
        return self.r, self.x


if __name__ == "__main__":
    N = 100000
    while True:
        points = [Point(r, x) for r, x in data.generate(N)]
        for i in range(10000):
            data.send([p.next() for p in points])
