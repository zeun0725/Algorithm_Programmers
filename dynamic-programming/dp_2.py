# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    pre = 1
    triangle.sort(key=lambda x: len(x), reverse=True)
    for tri in triangle[:-1]:
        for i, t in enumerate(triangle[pre]):
            triangle[pre][i] += max(triangle[pre - 1][i], triangle[pre - 1][i + 1])
        pre += 1

    return triangle[-1][-1]