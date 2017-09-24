#coding = utf-8
import sys

if __name__ == "__main__":
    #n = int(sys.stdin.readline().strip())
    #line = sys.stdin.readline().strip()
    line = "0 3 3 0 2 2 2 2 0 0 1 2 2 3 3 8 7 8 8 8"
    line = map(int, line.split(" "))
    line.sort()
    count = 0
    i = 0
    while i + 1 < len(line):
        if line[i] == 0:
            count += 1
            i += 1
            continue
        elif line[i] == line[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    if i < len(line) and line[i] == 0:
        count += 1
    print count
