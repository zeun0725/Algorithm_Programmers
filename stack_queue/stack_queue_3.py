# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586#


from collections import deque
import math
def solution(progresses, speeds):
    temp = 1
    answer = []
    pro = deque(math.ceil(p/s) for p, s in zip(map(lambda progress:100-progress,progresses),speeds))
    stand = pro.popleft()
    while pro:
        if stand >= pro[0]:
            pro.popleft()
            temp+=1
        else:
            answer.append(temp)
            stand = pro.popleft()
            temp=1
    answer.append(temp)

    return answer