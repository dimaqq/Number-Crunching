#!/usr/bin/env python
import struct
import random
import socket
import itertools

SENDBYTES = 65000
SENDPOINTS = int(SENDBYTES / 8)  # two floats

sock = None


def generate(N):
    """Generate N samples (r, x) where 2.4 > r > 4.0 and 0 > x > 1"""
    rv = [(random.random() * 2 + 2, random.random()) for i in range(int(1.3 * N))]
    return [b for b in rv if b[0] > 2.4][:N]


def sendraw(N, rawdata):
    global sock
    if not sock:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 70000)
    #print "sending", N, len(rawdata)
    header = struct.pack("q", N)
    sock.sendto(header + rawdata[:SENDBYTES], ("localhost", 6060))


def send(data, N=None):
    strdata = struct.pack("f" * 2 * min(len(data), SENDPOINTS), *itertools.chain.from_iterable(data[:SENDPOINTS]))
    sendraw(N or len(data), strdata)

if __name__ == "__main__":
    import sys
    import time
    sleep = float(sys.argv[1]) if sys.argv[1:] else 0
    N = 10000
    N = 100000
    while True:
        bigdata = [(random.random() * 2 + 2, random.random()) for i in range(int(1.3 * N))]
        bigdata = [b for b in bigdata if b[0] > 2.4][:N]
        bigdata = generate(N)
        for i in range(1000):
            send(bigdata)
            time.sleep(sleep)
            #print time.time()
            bigdata = [(r, r * x * (1 - x)) for r, x in bigdata]
