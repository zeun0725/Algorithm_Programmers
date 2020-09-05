# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    len_p = len(prices)
    answer = [0] * len_p
    for i in range(len_p):
        for j in range(i + 1, len_p):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer
# pop 으로 하려니까 효율성에서 초과 pop을 안하고 리스트 자체를 인덱스로 다가감