# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

# 다익스트라 개념 잘 정리되어 있는 곳
# https://mattlee.tistory.com/50

import heapq

def get_dijkstra(s, _fares):
    queue = []
    dist = {fare: float('inf') for fare in _fares}
    dist[s] = 0
    heapq.heappush(queue, [dist[s], s])
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if dist[cur_node] < cur_dist:
            continue
        for new_node, new_dist in _fares[cur_node].items():
            distance = cur_dist + new_dist
            if distance < dist[new_node]:
                dist[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    return dist

def init_fares(n, fares):
    _fares = dict()
    for _n in range(1, n + 1):
        _fares[_n] = {}
    for fare in fares:
        _fares[fare[0]].update({fare[1]: fare[-1]})
        _fares[fare[1]].update({fare[0]: fare[-1]})
    return _fares

def solution(n, s, a, b, fares):
    answer = float('inf')
    _fares = init_fares(n, fares)

    for _n in range(1, n+1):
        both_dist = get_dijkstra(s, _fares)[_n]
        each_dist = get_dijkstra(_n, _fares)
        answer = min(answer, both_dist + each_dist[a] + each_dist[b])

    return answer