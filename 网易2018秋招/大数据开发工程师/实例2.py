# -*- coding:utf-8 -*-
# 输入多个测试用例,每个测试用例第一行为整数n
#输出n阶方阵的和
#输入:
# 3
# 1 2 3
# 2 1 3
# 3 2 1
# 输出:
# 18

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        for v in values:
            ans += v
    print ans