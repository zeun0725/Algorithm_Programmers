# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import defaultdict

def create_graph(edge):
    graph = defaultdict(list)
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    return graph

def solution(n, edge):
    answer = 0
    graph = create_graph(edge)
    visited = [0] * n
    visited[0] = 1
    key_linked_list = graph[1]
    result = dict()

    while 0 in visited:
        answer += 1
        same_depth_list = []
        result[answer] = key_linked_list.copy()
        while key_linked_list:
            key = key_linked_list.pop(0)
            visited[key - 1] = 1
            for node in graph[key]:
                if visited[node - 1] == 0 and node not in key_linked_list and node not in same_depth_list:
                    same_depth_list += [node]
        key_linked_list = same_depth_list

    return len(result[max(result.keys())])
