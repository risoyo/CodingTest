import heapq
import sys
from random import randint


def findKthMax(l, k):
    if k > len(l):
        return
    key = randint(0, len(l) - 1)
    keyv = l[key]
    sl = [i for i in l[:key] + l[key + 1:] if i < keyv]
    bl = [i for i in l[:key] + l[key + 1:] if i >= keyv]
    if len(bl) == k - 1:
        return keyv
    elif len(bl) >= k:
        return findKthMax(bl, k)
    else:
        return findKthMax(sl, k - len(bl) - 1)


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n = sys.stdin.readline().strip()
    # line = "45 67 33 21"
    # n = "3"
    if line is "":
        print None
    elif n is "":
        print None
    else:
        line_split = map(int, line.split())
        n = int(n)
        print findKthMax(line_split, n)
