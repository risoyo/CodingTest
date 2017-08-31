#coding=utf-8
def every_num(num, key):
    count = 0
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            exclusive = num[i] ^ num[j]
            print num[i],num[j],exclusive
            if exclusive > key:
                count += 1
    return count

if __name__ == "__main__":
    # m = raw_input()
    # num = raw_input()
    m = "3 21845"
    num = "6 5 10"
    m = map(int, m.split(" "))
    num = map(int, num.split(" "))
    num.sort()
    i = 0
    for i in range(len(num)):
        if num[i] >= m[1]:
            break
    low = i*(i-1)/2
    total = m[0]*(m[0]-1)/2
    print total-low
