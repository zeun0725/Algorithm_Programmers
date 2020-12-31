def solution(s):
    try:
        int(s)
        if len(s) in [4, 6]:
            return True
        return False
    except:
        return False

    # for _s in s:
    #     if 48 <= ord(_s) <= 57:
    #         continue
    #     return False
    # if len(s) in [4,6]:
    #     return True
    # return False
    
