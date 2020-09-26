# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

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

