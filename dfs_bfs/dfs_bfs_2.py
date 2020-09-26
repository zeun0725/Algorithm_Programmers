# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

'''
def solution(n, computers):
    answer = 0
    network = []
    visited = [0] * n
    while 0 in visited:
        while network:
            std_com = network.pop(0)
            for idx, com in enumerate(computers[std_com]):
                if com == 1 and visited[idx] == 0:
                    network.append(idx)
                    visited[idx] = 1
        for idx, visit in enumerate(visited):
            if visit == 0:
                network.append(idx)
                visited[idx]=1
                answer += 1
                break
    return answer
'''


def dfs(start, visited, computers):
    if 0 not in visited:
        return 1
    for index, computer in enumerate(computers[start]):
        if visited[index] == 0 and computer == 1:
            visited[index] = 1
            dfs(index, visited, computers)
    return 1

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for idx, com in enumerate(computers):
        if visited[idx] == 0:
            answer += dfs(idx, visited, computers)
    return answer
