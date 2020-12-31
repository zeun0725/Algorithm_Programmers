# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

"""
방향그래프로 dfs 해서 모두 방문되면 경기 결과를 알 수 있음
진 방향 + 이긴 방향 해서 모두 연결 되면 알 수 있는 것
"""
from collections import defaultdict

def set_dic_value(results):
    win_dic = defaultdict(list)
    lose_dic = defaultdict(list)
    for result in results:
        win_dic[result[0] - 1] += [result[1] - 1]
        lose_dic[result[1] - 1] += [result[0] - 1]
    return win_dic, lose_dic

def dfs(value, rl, visited):
    stack = []
    visited[value] = 1
    stack += rl[value]
    while stack:
        next_val = stack.pop()
        visited[next_val] = 1
        if next_val in rl.keys():
            stack += [val for val in rl[next_val] if visited[val].__eq__(1)]
    return visited

def solution(n, results):
    win_dic, lose_dic = set_dic_value(results)
    answer = 0
    for val in range(n):
        visited = [0] * n
        if val in win_dic.keys():
            visited = dfs(val, win_dic, visited)
        if val in lose_dic.keys():
            visited = dfs(val, lose_dic, visited)
        if 0 not in visited:
            answer += 1
    return answer
