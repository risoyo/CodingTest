#coding = utf-8
import sys
if __name__ == "__main__":
    #num = int(sys.stdin.readline().strip())
    n = 1
    num = 169
    str_num = ''
    while len(str_num) < num:
        str_num += str('n' * 10)
        n = n + 1
    print str_num[-1]
    # if num == 0:
    #     print 0
    # elif num == 1:
    #     print 1
    # elif num == 2:
    #     print 2
    # elif num == 3:
    #     print 2
    # elif num == 4:
    #     print 3
    # elif int(num) > pow(10,12):
    #     n = 1414214
    #     while True:
    #         if int(num) > int(n*(n - 1)):
    #             n = n * 2
    #         elif int(num) < int(n*(n - 1)/2):
    #             n = n / 2
    #         elif int(n*(n - 1)/2) <= int(num) <= int(n*(n + 1)/2):
    #             break
    #         n = n+1
    #     print n
    # else:
    #     while True:
    #         if int(num) > int(n*(n - 1)):
    #             n = n * 2
    #             continue
    #         elif int(num) < int(n*(n - 1)/2):
    #             n = n / 2
    #             continue
    #         elif int(n*(n - 1)/2) <= int(num) <= int(n*(n + 1)/2):
    #             break
    #         n = n+1
    #     print n
