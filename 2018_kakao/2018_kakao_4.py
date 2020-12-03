# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

# 실행 루트 입력에서 w 삭제, w+c 있으면 사전등록 다시입력의 처음으로 돌아감

START = 65
END = 91


class DicLzw:
    def __init__(self):
        self.dic = {chr(eng): idx for idx, eng in enumerate(range(START, END), 1)}
        self.last_num = max(self.dic.values())

    def find_long_chr(self, msg):
        max_len = 0
        max_key = ''
        for key in self.dic.keys():
            if msg.startswith(key) and max_len < len(key):
                max_len = len(key)
                max_key = key
        return max_key, self.dic[max_key]

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
        max_str, ans = msg_dic.find_long_chr(msg)
        answer.append(ans)
        msg = msg.replace(max_str, "", 1)
        msg_dic.find_next_dic(msg, max_str)
    return answer