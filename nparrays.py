#!/usr/bin/env python
import data
import numpy


if __name__ == "__main__":
    N = 100000
    while True:
        points = [(r, x) for r, x in data.generate(N)]
        R = numpy.array([r for r, x in points])
        X = numpy.array([x for r, x in points])
        for i in range(100):
            points = [(R[idx], X[idx]) for idx in range(8000)]
            data.send(points, N=1000 * N)
            for j in range(1000):
                X = R * X * (1 - X)
