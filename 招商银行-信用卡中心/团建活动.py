# coding = utf-8
import sys


def total_tall(tall):
    total_a = 0
    total_b = 0
    flag = 0  # 0-a 1-b
    i = 0
    while i + 1 < len(tall):
        if flag == 0:
            if tall[i + 1] >= tall[i]:
                total_a += tall[i]
                total_a += tall[i + 1]
                i = i + 2
                flag = 1
            else:
                total_a += tall[i]
                i = i + 1
                flag = 1
        else:
            if tall[i + 1] >= tall[i]:
                total_b += tall[i]
                total_b += tall[i + 1]
                i = i + 2
                flag = 0
            else:
                total_b += tall[i]
                i = i + 1
                flag = 0
    if i < len(tall) - 1:
        if flag == 0:
            total_a += tall[-1]
        else:
            total_b += tall[-1]
    if total_b < total_a:
        return True
    else:
        return False


if __name__ == "__main__":
    # num = sys.stdin.readline().strip()
    # num = "3"
    # num = int(num)
    # tall = sys.stdin.readline().strip()
    # tall = "2 3 4 1 3 4 3 6 6 9 3 7 3 1 8 5 3"
    # tall = map(int, tall.split(" "))
    # result = total_tall(tall)
    # if result is True:
    #     print "true"
    # else:
    #     print "false"
    n = sys.stdin.readline().strip()
    n = map(int, n.split(" "))
    food = []
    for i in range(n[1]):
        line = sys.stdin.readline().strip()
        line = map(int, line.split(" "))
        food.append(line)
    print food
