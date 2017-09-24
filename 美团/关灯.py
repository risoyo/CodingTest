# coding=utf-8
import sys
import math


def f(x):
    return x ^ 1


if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # num = sys.stdin.readline().strip()
    num = map(int, num.split(" "))
    #本来不是这么写的,本来是按照下面的方法来写,但是总是超时
    #flag = 0  # 0-a 1-b
    # while sum(num) != 0:
    #     if flag == 0:
    #         flag = 1
    #         posi = num.index(1)
    #         num = map(f, num[posi:])
    #     else:
    #         flag = 0
    #         posi = num.index(1)
    #         num = map(f, num[posi:])
    # if flag == 1:
    #     print 'Alice'
    # else:
    #     print 'Bob'
    if num[-1] == 1:
        print 'Alice'
    else:
        print 'Bob'
