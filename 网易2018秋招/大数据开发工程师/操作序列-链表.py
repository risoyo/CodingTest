# -*- coding:utf-8 -*-
import sys
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 读取n
    line = sys.stdin.readline().strip()  # 读取第二行
    #n = 5
    #line = "1 2 3 4 5"
    num = line.split()
    link_list = ListNode(num[0])
    if n % 2 == 0:
        mark = 0
    else:
        mark = 1
    line_head = ListNode(num[0])
    line_tail = line_head
    for i in range(1, len(num)):
        if mark == 0:
            node = ListNode(num[i])
            node.next = line_head
            line_head = node
            mark = 1
            continue
        if mark == 1:
            node = ListNode(num[i])
            line_tail.next = node
            line_tail = line_tail.next
            mark = 0
            continue
    while line_head is not None:
        print line_head.val,
        line_head = line_head.next
