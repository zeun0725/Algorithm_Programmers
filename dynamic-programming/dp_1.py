# N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895



def solution(N, number):
    if N==number:
        return 1
    n_set =[{N}, {N-N, N+N, N*N, N//N, int(str(N)*2)}]
    if number in n_set[1]:
        return 2
    for idx in range(3,9):
        temp = set()
        temp.add(int(str(N)*idx))
        for i in range(0, idx//2):
            for x in n_set[i]:
                for y in n_set[idx-i-2]:
                    temp.add(x+y)
                    temp.add(x-y)
                    if y!=0:
                        temp.add(x//y)
                    if x!=0:
                        temp.add(y//x)
                    temp.add(x*y)
        if number in temp:
            return idx
        n_set.append(temp)

    return -1