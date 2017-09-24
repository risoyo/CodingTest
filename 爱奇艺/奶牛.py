import sys
n = int(raw_input())
x = sys.stdin.readline().strip()
x = x.split()
x = [int(i) for i in x]
num = sorted(x)
k = 1
for i in range(n):
    if num[i] - i > 0:
        k = k * (num[i] - i)
    else:
        k = 0
print k % 1000000007
# while 1:
#     try:
#         n = int(raw_input())
#         x = sys.stdin.readline().strip()
#         x = x.split()
#         x = [int(i) for i in x]
#         num = sorted(x)
#         k = 1
#         for i in range(n):
#             if num[i] - i > 0:
#                 k = k * (num[i] - i)
#             else:
#                 k = 0
#                 print k % 1000000007
#     except:
#         break
