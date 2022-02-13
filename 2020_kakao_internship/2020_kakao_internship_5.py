from collections import defaultdict

def dfs(visited, path, lead, trail):
    while 0 in visited:
        stand = path[0]
        for s in stand:
            if s in trail:
                if visited[lead[trail.index(s)]] == 1:
                    visited[s] = 1
                    stand = path[s]
                    break




def solution(n, path, order):
    _path = defaultdict(list)
    for p1, p2 in path:
        _path[p1].append(p2)
        _path[p2].append(p1)
    answer = True
    lead = []
    trail = []
    for _order in order:
        lead.append(_order[0])
        trail.append(_order[1])
    print(_path, lead, trail)
    visited = [0] * n
    dfs(visited, _path, lead, trail)
    return answer


if __name__ == "__main__":
    solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]) #true
    solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]) #true
    solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]) #false
