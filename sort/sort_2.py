# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746#


def solution(numbers):
    if set(numbers) == {0}: #모든 숫자가 0 일때
        return '0'
    max_len = max(numbers)
    max_len = len(str(max_len)) #가장 큰 수의 길이
    numbers = list(map(str, numbers)) #numbers 리스트 string 형태의 리스트로 바꿈

    # 숫자를 늘려서 비교 ex) max_len=2 , numbers = [1,20,3] 이면
    # nums = [('1','11'), ('20','20') , ('3','33')]
    nums = sorted([(number, number * (max_len - len(number) + 1)) for number in numbers], key=lambda x: x[1],
                  reverse=True) # 만든 수 정렬
    answer = ''
    answer += ''.join([x for x, y in nums])
    return answer