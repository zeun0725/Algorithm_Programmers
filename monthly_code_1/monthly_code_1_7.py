# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def get_ternary_code(n):
    tny_num = ''
    while n > 0:
        val = divmod(n, 3)
        n = val[0]
        tny_num += str(val[1])
    return int(tny_num)


def solution(n):
    answer = 0
    tny_n = str(get_ternary_code(n))[::-1]
    print(tny_n)
    for t in range(len(tny_n)-1,-1,-1):
        answer += (int(tny_n[t]) * (3**t))
    return answer

