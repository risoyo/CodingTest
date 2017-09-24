# coding = utf-8
import sys
#line = sys.stdin.readline().strip()
line = "frankfurt"
i = 0
while line[i+1:].count(line[i]) == 0:
    i += 1
line = line[i:]
count = 0
key = line[0]
num = line[1:].index(key)
line_split_1 = line[:line[1:].index(key)+1]
line_split_2 = line[line[1:].index(key)+1:]
# line_split_1 = list(line_split_1)
# line_split_2 = list(line_split_2)
for i in line_split_1:
    if line_split_2.count(i) != 0:
        count += 1
        line_split_2 = line_split_2[line_split_2.index(i)+1:]
print count * 2
