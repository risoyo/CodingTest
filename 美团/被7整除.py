# coding=utf-8
import sys
import itertools

if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # num = sys.stdin.readline().strip()
    # num = map(str, num.split(" "))
    n = 3
    num = ['127', '1996', '12']
    count = 0
    # for i in range(0, len(num)):
    #     for j in range(i + 1, len(num)):
    #         deal = is_7(num[i], num[j])
    #         if deal == 0:
    #             continue
    #         elif deal == 1:
    #             count += 1
    #         elif deal == 2:
    #             count += 2
    # num_list = list(itertools.permutations(num, 2))
    # num_list_1 = map(combine, num_list)
    for i in itertools.permutations(num, 2):
        if int(i[0] + i[1]) % 7 == 0:
            count += 1
    # for i in num_list:
    #     if i % 7 == 0:
    #         count += 1
    print count
