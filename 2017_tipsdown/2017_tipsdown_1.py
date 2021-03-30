# 짝 지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

### 정확성 효율성 고치기

def solution(s):
    if len(s) & 1 == 1:
        return 0
    stack = []
    for _s in s:
        if not stack:
            stack.append(_s)
            continue
        if stack[-1] == _s:
            stack.pop()
        else:
            stack.append(_s)

    if not stack:
        return 1
    return 0