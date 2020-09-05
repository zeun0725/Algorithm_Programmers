# K번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748


def sort_list(array,index):
    # list 정렬 후 원소 추출하는 함수
    array.sort()
    return array[index-1]

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sort_list(array[c[0]-1:c[1]],c[2]))
    return answer
