import sys

n = int(input())
if 1 <= n <= 1000000: pass
else: sys.exit()

num_lst = []
for _ in range(n):
    num = int(input())
    if abs(num) <= 1000000 and str(type(num)) == "<class 'int'>" and num not in num_lst: pass
    else: continue

    start = 0
    end = len(num_lst)

    while start < end:
        idx = int((start + end) / 2)
        if num > num_lst[idx]:
            start = idx + 1
        else:
            end = idx - 1

    idx = int((start + end) / 2)
    num_lst.insert(idx, num)

    for i in range(len(num_lst)):
        print(num_lst[i])