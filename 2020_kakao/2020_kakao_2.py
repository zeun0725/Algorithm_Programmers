# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def split_p(str_p):
    left, right = 0, 0
    for idx, p in enumerate(str_p):
        if p == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 균형잡힌 괄호 문자열
            return str_p[:idx + 1], str_p[idx + 1:]
    return str_p, ''


def compare_p(str_p): # 올바른 괄호 문자열 확인
    stack = []
    for p in str_p:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True if not stack else False


def solution(p):
    if p == '':
        return ''
    answer = ''
    u, v = split_p(p)
    if compare_p(u):
        answer += u
        return answer + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        u = u[1:-1]
        for u1 in u:
            if u1 == '(':
                temp += ')'
            else:
                temp += '('
        return temp
