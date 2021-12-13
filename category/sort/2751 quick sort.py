# 백준
# 카테고리별 문제 - 정렬
# 2751번 수 정렬하기 2번

import sys

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            # 조건문 순서가 바뀌면 코딩이 안된다..?
            # arr[left]가 마지막에 인덱싱 초과해버리기 떄문.
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)


n = int(input())
if 1 <= n <= 1000000: pass
else: sys.exit()


arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
    if abs(num) <= 1000000: pass
    else: sys.exit()

quick_sort(arr,0,len(arr)-1)
print(arr)
