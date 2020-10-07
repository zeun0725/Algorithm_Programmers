# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def compare_word(word, word2):
    return 1 if sum([0 if w1 == w2 else 1 for w1, w2 in zip(word, word2)]) == 1 else 0

def bfs(queue, words, target):
    answer = 0
    while queue:
        depth = len(queue)
        if target in queue:
            return answer
        while depth > 0:
            begin = queue.pop(0)
            queue += [words[idx] for idx, word in enumerate(words)
                      if compare_word(begin, word) == 1 and words[idx] not in queue]
            depth -= 1
        answer += 1
    return answer

def solution(begin, target, words):
    if target not in words:  # 단어 없을 때
        return 0
    return bfs([begin], words, target)

