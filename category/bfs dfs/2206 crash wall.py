#백준 1697번 숨바꼭질
#분류별 알고리즘 - DFS/BFS

import copy
import sys
from collections import deque

n, m = map(int,input().split())
if 1 <= n <= 1000 and 1 <= m <= 1000: pass
else: sys.exit()
maze = []
for _ in range(n):
    maze.append(list(input()))
maze[0][0] = 1
go_x = [-1,1,0,0]
go_y = [0,0,-1,1]


def bfs(x, y, maze):
    lst = copy.deepcopy(maze)
    lst[x][y] = 0
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            dx = x + go_x[i]
            dy = y + go_y[i]
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy]:
                    print(dx, dy)
                    lst[dx][dy] = lst[x][y] + 1
                    queue.append([dx, dy])
                    visited[dx][dy] = True

    if visited[n-1][m-1]:
        return lst[n-1][m-1]
    else:
        return -1


cnt_lst = set([])
for i in range(n):
    for j in range(m):
        if maze[i][j] == 1:
            visited = [[False] * m for _ in range(n)]
            temp = bfs(i, j, maze)
            cnt_lst.add(temp)
print(min(cnt_lst))