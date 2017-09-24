# coding = utf-8
import sys


def lcm(num):
    x = num[0]
    y = num[1]
    if x > y:
        greater = x
    else:
        greater = y
    lcm = []

    while greater <= num[2]:
        if (greater % x == 0) and (greater % y == 0):
            lcm.append(greater)
        greater += 1

    return len(lcm)


if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    #n = "1 1 10"
    n = map(int, n.split(" "))
    print lcm(n)
