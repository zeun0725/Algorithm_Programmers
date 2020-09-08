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


# testcase 1번 시간초과 나온 답
'''
import itertools
from collections import defaultdict
from functools import reduce 
def solution(clothes):
    answer = len(clothes)
    dic_clo=defaultdict(int)
    for cloth, category in clothes:
        dic_clo[category]+=1
    if len(dic_clo)==1:
        return answer
    for i in range(2,len(dic_clo)+1):
        p = itertools.combinations(dic_clo.values(),i)
        for i in p:
            answer+=reduce(lambda x,y:x*y,i)   
    return answer
'''

# 그 이후로 푼 답
'''
import itertools
from collections import defaultdict
from functools import reduce 

def solution(clothes):
    answer = 1
    dic_clo=defaultdict(int)
    for cloth, category in clothes:
        dic_clo[category]+=1
    for i in dic_clo.values():
        answer*=(i+1)
    
    return answer-1
'''