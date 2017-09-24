# coding=utf-8
import sys
import itertools
import threading
def judge_u():
    pass
def judge_5():
    pass
def judge_1():
    pass
threads = []
t1=threading.Thread(target=judge_u())
threads.append(t1)
t2=threading.Thread(target=judge_5())
threads.append(t2)
t3=threading.Thread(target=judge_1())
threads.append(t3)
if __name__ == "__main__":
    i=0
    # for t in threads:
    #     t.start()
    flag = 0
    count = 0
    while i<=200000:
        n = sys.stdin.readline().strip()
        if n == 'u':
            flag = 1
            continue
        elif flag == 1 and n == '5':
            flag = 2
            continue
        elif flag ==2 and n == '1':
            count +=1
            continue
        else:
            flag = 0
    print count
