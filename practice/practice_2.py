def solution(strings, n):
    return sorted(strings, key=lambda x: x[n])


#print(solution(['abc','abcde','ba', 'bbb','aa', 'ab'],1))
strings = [123,12,456,123345]
print(sorted(strings,reverse=True))

sss = [123,12,456,123345]
print(sorted(strings, key=lambda x: -x))