# -*- coding:utf-8 -*-
# 小易有一个圆心在坐标原点的圆，小易知道圆的半径的平方。小易认为在圆上的点而且横纵坐标都是整数的点是优雅的，小易现在想寻找一个算法计算出优雅的点的个数，请你来帮帮他。
# 例如：半径的平方如果为 25
# 优雅的点就有：(+/-3, +/-4), (+/-4, +/-3), (0, +/-5) (+/-5, 0)，一共 12 个点。
# 输入描述:
# 输入为一个整数，即为圆半径的平方,范围在32位int范围内。
#
#
# 输出描述:
# 输出为一个整数，即为优雅的点的个数
#
# 输入例子 1:
# 25
#
# 输出例子 1:
# 12
import math
# int(-r)
if __name__ == "__main__":
    n = int(raw_input())
    r = math.sqrt(n)
    count = 0
    count2 = 0
    count3 = 0
    for i in range(int(-r), int(r)+1):  # 遍历半径范围内(-r,r)的所有点,找到圆上的点
        for j in range(int(-r), int(r) + 1):
            if i * i + j * j == n:
                count2 += 1
    for i in range(1, int(r)+1):  # 遍历四分之一象限的点(1,r),后面要对count输出控制,四倍之后要加上(0,+-r)四个点
        for j in range(1, int(r) + 1):
            if i * i + j * j == n:
                count += 1
    i = 0
    while i ** 2 <= n / 2:  # 减少遍历次数,使用x**2+y**2=r**2这一性质
        j_square = n - i ** 2
        j = int(math.sqrt(j_square))
        if j ** 2 == n - i ** 2:
            if i == 0 or i == j:
                count3 += 4
            else:
                count3 += 8
        i += 1
    if int(r) == r:
        print count*4+4
    else:
        print count*4
    print count2
    print count3
