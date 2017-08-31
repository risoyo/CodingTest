# -*- coding:utf-8 -*-
import sys


def max_seq(a, n):
    max_sum = maxi = a[0]
    for i in range(1, n):
        if maxi <= 0:
            maxi = a[i]
        else:
            maxi += a[i]
        if maxi > max_sum:
            max_sum = maxi
    return max_sum


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    line_split = map(int, line.split())
    print max_seq(line_split, len(line_split))
