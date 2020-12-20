# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3#

def solution(routes):
    answer = 1
    routes.sort(key=lambda x: (x[0], -x[1]))
    end = routes[0][1]
    for route in routes[1:]:
        if route[0] <= end:
            if end > route[1]:
                end = route[1]
            continue
        answer += 1
        end = route[1]
    return answer

