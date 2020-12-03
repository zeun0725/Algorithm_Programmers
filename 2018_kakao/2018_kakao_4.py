# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

START = 65
END = 91


class DicLzw:
    def __init__(self):
        self.dic = {chr(eng): idx for idx, eng in enumerate(range(START, END), 1)}
        self.last_num = max(self.dic.values())

    def find_long_chr(self, msg):
        if msg in self.dic.keys():
            return len(msg), self.dic[msg]

        for idx, _ in enumerate(msg, 1):
            if msg[:idx] in self.dic.keys():
                continue
            return idx - 1, self.dic[msg[:idx - 1]]

    def find_next_dic(self, msg, token):
        for idx, _ in enumerate(msg, 1):
            if token + msg[:idx] in self.dic.keys():
                continue
            else:
                self.last_num += 1
                self.dic[token + msg[:idx]] = self.last_num
                break


def solution(msg):
    answer = []
    msg_dic = DicLzw()

    while msg:
        """
        반복적 루트
        1. 가장 긴 단어 찾기
        2. 찾은 단어 출력
        3. 찾은 단어 입력에서 제거
        4. 새로운 단어 찾아 사전 등록
        """
        max_len, ans = msg_dic.find_long_chr(msg) #1
        answer.append(ans) #2
        max_str = msg[:max_len]
        msg = msg[max_len:] #3
        msg_dic.find_next_dic(msg, max_str) #4

    return answer
