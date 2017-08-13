# -*- coding:utf-8 -*-
import sys
from itertools import chain
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 读取n
    line = sys.stdin.readline().strip()  # 读取第二行
    #n = 5
    #line = "1 2 3 4 5"
    line_split = line.split()
    line_new = []
    line_top = []
    # for i in range(0,len(line_split)):
    #     line_new.append(line_split[i])
    #     line_new.reverse()
    # for i in line_new:
    #     print i,
    if n % 2 == 0:
        mark = 0
    else:
        mark = 1
    line_new.append(line_split[0])
    for i in range(1, len(line_split)):
        if mark == 0:
            line_top.append(line_split[i])
            mark = 1
            continue
        if mark == 1:
            line_new.append(line_split[i])
            mark = 0
            continue
    line_top.reverse()
    for i in line_top:
        print i,
    for i in line_new:
        print i,