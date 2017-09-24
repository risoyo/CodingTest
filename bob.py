# coding=utf-8
import sys


def step(num):
    d = [0 for i in range(num+1)]
    d[1] = 1
    d[2] = 1
    for i in range(3, num+1):
        d[i] = d[i - 1] + d[i - 2]
    return d[num]


if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    n = int(n)
    num_collect = []
    num_result = []
    for i in range(n):
        num = int(sys.stdin.readline().strip())
        num_collect.append(num)
    for i in num_collect:
        num_result.append(step(i))
    for i in num_result:
        print i
