#coding=utf-8
import sys
if __name__ == "__main__":
    # n = raw_input()
    # num = raw_input()
    n = "3"
    num = "6 2 1"
    n = int(n)
    num = map(int, num.split(" "))
    for i in num:
        sys.stdout.write('%d' % i)