import sys


def ackermann():
    m, n = int(sys.argv[1]), int(sys.argv[2])
    print(m + n + 1)
    return m + n + 1
