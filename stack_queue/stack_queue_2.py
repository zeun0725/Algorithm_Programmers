# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    sum_weight = 0  # 다리 위에 있는 트럭 무게 합
    time = 0  # 시간
    trucks = []  # 다리 위에 있는 트럭

    push_index = 0
    pop_index = 0

    len_truck = len(truck_weights)

    while pop_index != len_truck:  # 모든 트럭이 다리를 건너기 전까지
        time += 1
        if trucks and trucks[0] + bridge_length == time:
            # 트럭이 다리를 다 건넜을 때
            trucks.pop(0)
            sum_weight -= truck_weights[pop_index]
            pop_index += 1
        if push_index < len_truck and sum_weight + truck_weights[push_index] <= weight:
            # 다리가 새로운 트럭의 무게까지 견딜 수 있을 때
            sum_weight += truck_weights[push_index]
            trucks.append(time)
            push_index += 1

    return time


from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck = deque(truck_weights)
    bridge = deque([])
    _weight = 0
    while truck:
        time += 1
        if bridge and time - bridge[0][1] == bridge_length:
            _weight -= bridge[0][0]
            bridge.popleft()
        if _weight + truck[0] <= weight:
            _weight += truck[0]
            bridge.append([truck.popleft(), time])

    return time+bridge_length
















