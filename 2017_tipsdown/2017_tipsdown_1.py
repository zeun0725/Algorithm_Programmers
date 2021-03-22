# 짝 지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

### 정확성 효율성 고치기
def solution(s):
    if len(s) & 1 == 1:
        return 0

    while True:
        if s[0] == s[1]:
            s = s[2:]
        else:
            break
    while True:
        if s[-1] == s[-2]:
            s = s[:-2]
        else:
            break
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if s1[::-1] == s2:
        return 1
    return 0
