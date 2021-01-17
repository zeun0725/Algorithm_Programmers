# 징검다리
# https://programmers.co.kr/learn/courses/30/lessons/43236


def make_ge_mid_num(distance, mid, n):
    sum_dist = distance[0]
    for dist in distance[1:]:
        if sum_dist < mid:
            sum_dist += dist
            n -= 1
        else:
            sum_dist = dist
    return n


def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.extend([0, distance])
    rocks.sort()
    r_distance = [rocks[idx] - rocks[idx - 1] for idx, rock in enumerate(rocks[1:], 1)]

    while left <= right:
        mid = (left + right) // 2
        rm_n = make_ge_mid_num(r_distance, mid, n)
        if rm_n < 0:
            right = mid - 1
        else:
            left = mid + 1
            answer = max(mid, answer)
    return answer