# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578#


# 수학적으로 접근
# 각 카테고리 개수에 +1 해줌 (안고르는 경우를 위해)
# 그 후 모두 안고른 경우만 빼줌, 마지막 결과에 (-1)
from functools import reduce
from collections import Counter

def solution(clothes):
    return reduce(lambda x, y: x * y,
                  map(lambda x: x + 1,
                      Counter(category for cloth, category in clothes).values()))-1


#==============================
from collections import Counter
from functools import reduce
def solution(clothes):
    return reduce(lambda x, y: x * y, map(lambda x: x + 1, Counter([clothe[1] for clothe in clothes]).values())) - 1
