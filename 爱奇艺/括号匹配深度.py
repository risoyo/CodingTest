# coding = utf-8
import sys


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


line = sys.stdin.readline().strip()
length = len(line)
i = 0
ans = 0
flag = 0
st = Stack()
for i in range(0, length):
    if line[i] == '(':
        st.push(line[i])
    if st.size() > ans:
        ans = st.size()
    if st.size() == 0 and line[i] == ')':
        flag = 1
        break
    if st.size() != 0 and line[i] == ')':
        st.pop()
if flag == 1 or st.size() != 0:
    print 0
else:
    print ans
