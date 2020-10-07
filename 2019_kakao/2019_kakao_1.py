# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3


def solution(record):
    user_info = dict()
    answer = []
    for rec in record:
        rec_list = rec.split(" ")
        if rec_list[0] == "Enter":
            user_info[rec_list[1]] = rec_list[2]
            answer.append(rec_list[1]+" 들어왔습니다.")
        elif rec_list[0] == "Change":
            user_info[rec_list[1]] = rec_list[2]
        else:
            answer.append(rec_list[1]+" 나갔습니다.")
    answer2=[]
    for a in answer:
        t = a.split(" ")
        answer2.append('{0}님이 {1}'.format(user_info[t[0]], t[1]))
    return answer2