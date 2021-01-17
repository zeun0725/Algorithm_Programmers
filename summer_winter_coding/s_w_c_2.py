# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [list(map(lambda x: x+1, divmod(idx, n)[::-1])) for idx, word in enumerate(words[1:], 1) if words[idx-1][-1].__ne__(words[idx][0]) or word in words[:idx]]
    return [0, 0] if not answer else answer[0]


def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    mid = (left + right) // 2
    rocks.extend([0, distance])
    rocks.sort()
    r_distance = [rocks[idx] - rocks[idx - 1] for idx, rock in enumerate(rocks[1:], 1)]

    while left <= right:
        rm_n = n
        sum_dist = 0
        for d in r_distance:
            if sum_dist < mid:
                sum_dist += d
                rm_n -= 1
            else:
                sum_dist = d
        if rm_n > 0:
            right = mid - 1
            answer = max(mid, answer)
        else:
            left = mid + 1
            answer = max(mid, answer)

    return answer