# n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

def get_number(n, value): # 진법 출력
    r_set = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
             13: 'D', 14: 'E', 15: 'F'}
    val = ''
    q = n
    while q >= n:
        q, r = divmod(value, n)
        val += r_set[r]
        value = q
    if q.__ne__(0):
        val += r_set[q]
    return val[::-1]


def get_answer(p, t, m, value):
    answer = ''
    for idx in range(p-1, t * m, m):
        if len(answer).__eq__(t):
            break
        answer += value[idx]
    return answer


def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    max_tern = 0
    value = ''
    while max_tern <= t * m:
        value += get_number(n, max_tern)
        max_tern += 1
    return get_answer(p, t, m, value)
