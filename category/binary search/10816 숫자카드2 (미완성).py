# 백준
# 카테고리별 문제 - 이분탐색
# 10816 숫자카드 2
# 시간제한 1초
# 순차탐색을 사용하면 시간복잡도가 250억이므로 불가.
# for 문 + 이진탐색 + del + sorted
# (500,000 * 19) * 2 + 500,000 = 19,500,000
import sys


def binary_search(arr,target,start,end):
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            cnt += 1
            del arr[mid]
            start = 0
            end = len(arr)-1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return cnt


# 수의 범위를 제한시켜주는 함수
def num_restrict(x,a,b):
    if x<a or x>b:
        sys.exit()


n = int(input())
num_restrict(n,1,500000) # 1 <= n <= 500,000
n_lst = sorted(list(map(int,sys.stdin.readline().split())))
m = int(input())
num_restrict(n,1,500000) # 1 <= m <= 500,000
m_lst = list(map(int,sys.stdin.readline().split()))
for i in m_lst:
    print(binary_search(n_lst,i,0,len(n_lst)-1), end=' ')