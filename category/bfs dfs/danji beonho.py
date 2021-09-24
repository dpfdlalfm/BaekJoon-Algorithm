from collections import deque
import sys

n = int(input())
if 5 <= n <= 25:pass
else: sys.exit()

aparts = []
for _ in range(n):
    aparts.append(list(input()))

visited = [[False] * n for _ in range(n)]
print(visited)


def move(i,j):
    cnt = 0
    while cnt < 4:
        if i < 0 or i > n or j < 0 or j > n:
            continue


def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        if i+1 <= n and aparts[i+1][j] == '1' and not visited[i+1][j]:
            visited[i+1][j] = True
            queue.append([i,j+1])
        if i-1 >= 0 and aparts[i-1][j] == '1' and not visited[i-1][j]:
            visited[i-1][j] = True
            queue.append([i-1,j])
        if j+1 <= n and aparts[i][j+1] == '1' and not visited[i][j+1]:
            visited[i][j+1] = True
            queue.append([i,j+1])
        if i-1 >= 0 and aparts[i][j-1] == '1' and not visited[i][j-1]:
            visited[i][j-1] = True
            queue.append([i,j-1])


for i in range(n):
    for j in range(n):
        if aparts[i][j] == '1' and not visited[i][j]:
            bfs(i,j)