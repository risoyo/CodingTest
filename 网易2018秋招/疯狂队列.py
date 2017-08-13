# -*- coding:utf-8 -*-
import sys
import math

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 读取n
    line = sys.stdin.readline().strip()  # 读取第二行
    line_split = line.split()
    line_split = map(int, line_split)
    line_split.sort()
    line_new = [line_split[-1]]
    if n == 0:
        print 0
    elif n == 1:
        print 0
    else:
        mark = 1
        count = 0
        for i in range(0,len(line_split)-1):
                if mark == 0:
                    line_new.insert(0, line_split[i])
                    mark = 1
                    continue
                if mark == 1:
                    line_new.insert(len(line_new), line_split[i])
                    mark = 0
                    continue
        for i in range(1, len(line_new)):
            count += math.fabs(line_new[i-1] - line_new[i])
        print int(count)