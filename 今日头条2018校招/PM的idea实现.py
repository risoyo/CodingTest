#coding=utf-8
import sys
if __name__ == "__main__":
    # total = raw_input()
    # idea = raw_input()
    # idea_collect = []
    # total = map(int, total.split(" "))
    # for i in range(total[2]):
    #     idea = raw_input()
    #     idea = map(int, idea.split(" "))
    #     idea_collect.append(idea)
    total = "2 2 5"
    idea_collect = [[3, 1, 2], [3, 2, 1], [3, 2, 2], [3, 1, 1]]
    compelete = [0 for col in range(len(idea_collect))]
    idea_collect.sort(key=lambda x: (x[1], -x[2]))
    print idea_collect
