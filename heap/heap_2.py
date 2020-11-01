# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

def min_rm(queue):
    if not queue:
        return queue
    return queue.remove(min(queue))


def max_rm(queue):
    if not queue:
        return queue
    return queue.remove(max(queue))


def solution(operations):
    queue = []
    for operation in operations:
        oper = operation.split(" ")
        if oper[0] == 'I':
            queue.append(int(oper[-1]))
        elif oper[0] == 'D' and oper[-1] == '-1':
            min_rm(queue)
        elif oper[0] == 'D' and oper[-1] == '1':
            max_rm(queue)
    if not queue:
        return [0, 0]
    return [max(queue), min(queue)]
