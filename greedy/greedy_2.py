# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883#

def solution(number, k):
    if int(number) == 0:  # number = "00000..."
        return '0'

    if len(set(number)) == 1:  # number = "99999..."
        return number[:-k]

    answer = []
    for num in number[:]:
        while answer and answer[-1] < num and k > 0:
            # answer 안 마지막 값이 num 보다 작을때 pop
            answer.pop()
            k -= 1
        answer.append(num)  # 일단 push

    if k > 0:  # for문을 다 돌았지만 제거할 수가 아직 더 남았을 때
        answer = answer[:-k]  # k 전까지 수로

    return ''.join(answer)