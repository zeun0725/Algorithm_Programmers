# 풍선 터트리기

# 한번만 번호가 작은 풍선 터트릴 수 있음

def solution(a):
    answer = 0

    for _idx, _a in enumerate(a):
        l_min = None
        r_min = None
        penalty = False
        if _idx != 0:
            l_min = min(a[:_idx])
            if l_min < _a:
                penalty = True
        if _idx != len(a) - 1:
            r_min = min(a[_idx+1:])
            if r_min < _a and penalty:
                continue
        answer += 1
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))