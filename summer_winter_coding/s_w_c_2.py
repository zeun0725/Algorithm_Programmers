# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [list(map(lambda x: x+1, divmod(idx, n)[::-1])) for idx, word in enumerate(words[1:], 1) if words[idx-1][-1].__ne__(words[idx][0]) or word in words[:idx]]
    return [0, 0] if not answer else answer[0]
