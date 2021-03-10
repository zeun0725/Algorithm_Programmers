#삼각 달팽이
import itertools

def solution(n):
    answer = [[0 for _ in range(_n)] for _n in range(1, n+1)]

    i = 1
    s_idx = 0
    e_idx = -1
    while n > 0:
        for ans in range(s_idx, n):
            if answer[ans][s_idx] == 0:
                answer[ans][s_idx] = i
                i += 1
        for ans in range(1, len(answer[e_idx])):
            if answer[e_idx][ans] == 0:
                answer[e_idx][ans] = i
                i += 1
        for ans in range(n-1, abs(e_idx), -1):
            if answer[ans][e_idx] == 0:
                answer[ans][e_idx] = i
                i += 1
        s_idx += 1
        e_idx -= 1
        n -= 1
    ans = list(itertools.chain(*answer))
    return ans