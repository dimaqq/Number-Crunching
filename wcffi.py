#!/usr/bin/env python
import data
import cffi
ffi = cffi.FFI()
ffi.cdef("""float nextN(float, float, int);""")
libx = ffi.dlopen("./libwcffi.so")


if __name__ == "__main__":
    N = 100000
    while True:
        points = [(r, x) for r, x in data.generate(N)]
        for i in range(100):
            data.send(points, N=1000 * len(points))
            for idx, (r, x) in enumerate(points):
                points[idx] = r, libx.nextN(r, x, 1000)
