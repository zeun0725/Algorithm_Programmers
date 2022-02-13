# 트리 트리오 중간값

from itertools import combinations

def get_combinaton(n):
    node = [_n for _n in range(1, n+1)]
    combi_list = list(combinations(node, 3))
    return combi_list

def bfs(s,e,edges,dist, visited):
    visited[s-1] = 1
    for edge in edges:
        if s == edge[0] and visited[edge[1]-1] == 0:
            if e == edge[1]:
                return dist + 1
            return bfs(edge[1],e,edges,dist+1, visited)
        elif s == edge[1] and visited[edge[0]-1] == 0:
            if e == edge[0]:
                return dist + 1
            return bfs(edge[0],e,edges,dist+1, visited)

    return dist

def solution(n, edges):
    answer = -1
    n_list = get_combinaton(n)
    dist_save = [[-1 for _ in range(n)] for _n in range(n)]
    for a, b, c in n_list:
        if dist_save[a-1][b-1] != -1:
            v1 = dist_save[a-1][b-1]
        else:
            v1 = bfs(a, b, edges, 0, [0]*n)

            dist_save[a-1][b-1] = v1
            dist_save[b-1][a-1] = v1

        if dist_save[b - 1][c - 1] != -1:
            v2 = dist_save[b - 1][c - 1]
        else:
            v2 = bfs(b, c, edges, 0, [0] * n)
            dist_save[b - 1][c - 1] = v2
            dist_save[c - 1][b - 1] = v2

        if dist_save[a-1][c-1] != -1:
            v3 = dist_save[a-1][c-1]
        else:
            v3 = bfs(a, c, edges, 0, [0]*n)
            dist_save[a-1][c-1] = v3
            dist_save[c-1][a-1] = v3
        ans = sorted([v1, v2, v3])[1]
        if answer < ans:
            answer = ans
    return answer

solution(5, [[1,5],[2,5],[3,5],[4,5]])
