#coding=utf-8
if __name__ == "__main__":
    num = raw_input()
    point_collect = []
    num = int(num)
    for i in range(num):
        point = raw_input()
        point = map(int, point.split(" "))
        point_collect.append(point)
    # num = "5"
    # point_collect = [[1, 2], [5, 3], [4, 6], [7, 5], [9, 0]]
    max_point = []
    point_collect.sort()
    x_array = point_collect[len(point_collect)/2 + 1:-1]
    max_point.append(point_collect[-1])
    point_collect.sort(key=lambda x:x[1])
    y_array = point_collect[len(point_collect)/2 + 1:-1]
    max_point.append(point_collect[-1])
    com_array = [i for i in x_array if i in y_array]
    for i in com_array:
        max_point.append(i)
    max_point.sort()
    for i in max_point:
        print i[0],
        print i[1]

