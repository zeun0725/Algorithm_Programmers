# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747#



def solution(citations):
    h_index = max(citations)
    citations.sort(reverse=True)
    len_c = len(citations)

    while h_index > 0:
        papers = sum([1 for i in citations if i>=h_index]) #인용된 논문 개수
        if papers >= h_index and len_c - papers <= h_index:
            #인용된 논문 개수가 h_index 이상이고 나머지 논문이 h_index 이하일 때 => 정답
            return h_index
        h_index-=1

    return h_index