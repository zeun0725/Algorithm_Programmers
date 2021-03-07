from collections import defaultdict

def get_min_idx(visited, dist, n):
    min_dist = 100000
    min_idx = -1
    for _n in range(1, n + 1):
        if _n not in visited and dist[_n - 1] <= min_dist:
            min_dist = dist[_n - 1]
            min_idx = _n
    return min_idx

def get_dijkstra(s, d, _fares, n):
    visited = [s]
    dist = init_dist(_fares[s], s, n)
    s = get_min_idx(visited, dist, n)
    while len(visited) != n:
        visited.append(s)
        queue = _fares[s].items()
        for key, val in queue:
            dist[key-1] = min(dist[key-1], dist[s-1] + val)
        s = get_min_idx(visited,dist, n)
    return dist

def init_dist(fare_s, s, n):
    dist = [100000] * n
    dist[s - 1] = 0
    for key, val in fare_s.items():
        dist[key - 1] = val
    return dist

def solution(n, s, a, b, fares):
    answer = 100000000
    _fares = dict()
    for _n in range(1, n+1):
        _fares[_n] = {}
    for fare in fares:
        _fares[fare[0]].update({fare[1]: fare[-1]})
        _fares[fare[1]].update({fare[0]: fare[-1]})
    for _n in range(1, n+1):
        answer = min(answer, get_dijkstra(s, _n, _fares, n)[_n-1] + get_dijkstra(_n, a, _fares,n)[a-1] + get_dijkstra( _n, b, _fares, n)[b-1])
    return answer




solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])