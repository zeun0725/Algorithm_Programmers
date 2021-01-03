# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258#
"""
처음 풀이
단순히 처음부터 탐색하며 가장 구간이 짧고 시작 진열대 번호가 작은 것을 리턴해주었음
https://tech.kakao.com/2020/07/01/2020-internship-test/
카카오 테크 문제 해설을 보고 코드 수정
투 포인터 이용
"""
# def solution(gems):
#     gems_set = set(gems)
#     gems_set_len = gems_set.__len__()
#     answer = []
#     gems_len = gems.__len__()
#     for gem in range(gems_len):
#         temp_ans = []
#         for i, g in enumerate(gems[gem:], gem):
#             if g not in temp_ans:
#                 temp_ans.append(g)
#             if temp_ans.__len__()==gems_set_len:
#                 answer.append([gem+1,i+1,i-gem])
#                 break
#     answer.sort(key=lambda x: (x[2],x[0]))
#
#     return answer[0][:2]


from collections import defaultdict
def solution(gems):
    gem_cnt = defaultdict(int)
    l_point = 0
    r_point = 0
    set_gem_len = set(gems).__len__()
    gem_len = gems.__len__()
    answer = []
    while -1 < l_point <= gem_len and -1 < r_point <= gem_len:
        if gem_cnt.keys().__len__().__lt__(set_gem_len):
            if r_point.__ne__(gem_len):
                gem_cnt[gems[r_point]] += 1
            r_point += 1
            continue
        if gem_cnt.keys().__len__().__eq__(set_gem_len):
            if gem_cnt[gems[l_point]].__eq__(1):
                gem_cnt.pop(gems[l_point])
                answer.append([l_point+1, r_point, r_point-l_point])
            else:
                gem_cnt[gems[l_point]] -= 1
            l_point += 1
            continue

    answer.sort(key=lambda x: (x[2], x[0]))
    return answer[0][:2]

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])