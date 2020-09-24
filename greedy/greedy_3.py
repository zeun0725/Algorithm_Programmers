# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
                "X": 23, "Y": 24, "Z": 25}
    # N 이 딱 중간
    temp_sum_value = [min(alphabet[n], 26 - alphabet[n]) for n in name]
    idx = 0
    answer = 0

    while 1:
        left = -1
        right = 1
        answer += temp_sum_value[idx]
        temp_sum_value[idx] = 0
        if sum(temp_sum_value) == 0:
            return answer

        while temp_sum_value[idx + left] == 0:
            # 가장 가까운 left 값 찾기
            left -= 1
        while temp_sum_value[idx + right] == 0:
            # 가장 가까운 right 값 찾기
            right += 1

        answer += abs(left) if abs(left) < right else right
        idx += left if abs(left) < right else right
    return answer