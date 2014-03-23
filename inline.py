#!/usr/bin/env python
import data


if __name__ == "__main__":
    N = 100000
    while True:
        points = [(r, x) for r, x in data.generate(N)]
        for i in range(100):
            data.send(points, N=100 * len(points))
            for idx in range(len(points)):
                r, x = points[idx]
                for j in range(100):
                    x = r * x * (1 - x)
                points[idx] = r, x
