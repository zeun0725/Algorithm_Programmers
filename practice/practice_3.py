def solution(arr):
    ans = [arr[0]]
    for _arr in arr:
        if ans[-1].__ne__(_arr):
            ans.append(_arr)
    return ans