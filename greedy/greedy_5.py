# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861#

def solution(n, costs):
    if n == 1:  # 섬 1개일 때
        return 0
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    connect = set()  # 연결된 노드 담을 곳
    while len(connect) < n:  # 모든 노드가 연결될때까지
        for idx, cost in enumerate(costs):
            if cost[0] in connect and cost[1] in connect:
                # 이미 연결돼있으면 무시
                continue
            if not list(connect) or cost[0] in connect or cost[1] in connect:
                # 연결
                value = costs.pop(idx)
                connect.add(value[0])
                connect.add(value[1])
                answer += value[2]
                break
    return answer
