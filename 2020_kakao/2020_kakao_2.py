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

    
# 2번째 풀이

from collections import deque 

def get_balc_str(w):
    for _w in range(2,len(w) + 1,2):
        if w[:_w].count('(') == w[:_w].count(')'):
            return w[:_w], w[_w:]

def is_right_str(u):
    stack = deque([])
    for _u in u:
        if _u == '(':
            stack.append(_u)
            continue
        if stack:
            stack.popleft()
        else:
            return False
    return True

def set_right_u(u):
    new_u = [')' if _u =='(' else '(' for _u in u[1:-1]]
    return ''.join(new_u)
    

def solution(p):
    if not p:
        return ''
    answer = ''
    if is_right_str(p):
        return p
    u, v = get_balc_str(p)
    if is_right_str(u):
        answer += u + solution(v)
    else:
        u = set_right_u(u)
        answer += '(' + solution(v) + ')' + u

    return answer
