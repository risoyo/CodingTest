import sys
if __name__ == "__main__":
    # id = sys.stdin.readline().strip()
    # important = sys.stdin.readline().strip()
    id = '1 2 3 3 1 2 2'
    important = '2 1 1 1 1 1 1'
    id = map(int,id.split(" "))
    important = map(int,important.split(" "))
    print id
    print important
    max_num = max(id)
    elec = [0 for i in range(max_num+1)]
    for i in range(len(id)):
        elec[id[i]] += id[i] * important[i]
    elec_im = max(elec)
    print elec.index(elec_im)
