#!/usr/bin/env python
import data


def next(p):
    r, x = p
    x = r * x * (1 - x)
    return (r, x)


if __name__ == "__main__":
    N = 100000
    while True:
        points = [(r, x) for r, x in data.generate(N)]
        for i in range(10000):
            data.send(points)
            points = [next(p) for p in points]
