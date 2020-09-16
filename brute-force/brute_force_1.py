# https://programmers.co.kr/learn/courses/30/lessons/42840#
# 모의고사

def solution(answers):
    # -----------------------------
    # 필요한 변수 선언 부
    answer = [0] * 3

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_l = len(one)
    two_l = len(two)
    three_l = len(three)

    ans_len = len(answers)

    # -----------------------------
    # 각 수포자의 답지 정답 length 만큼 복사
    one = one * (ans_len // one_l) + one[:ans_len % one_l]
    two = two * (ans_len // two_l) + two[:ans_len % two_l]
    three = three * (len(answers) // three_l) + three[:len(answers) % three_l]

    # -----------------------------
    # 각 수포자 답지 비교
    for o1, t1, t2, a in zip(one, two, three, answers):
        if a - o1 == 0:
            answer[0] += 1
        if a - t1 == 0:
            answer[1] += 1
        if a - t2 == 0:
            answer[2] += 1

    max_ans = max(answer)

    return [i + 1 for i, a in enumerate(answer) if a == max_ans]