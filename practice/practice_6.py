def solution(n):
    return list(map(int, str(n)[::-1]))


def solution(prices):
    answer = []
    for idx, _ in enumerate(prices[:-1]):
        idx_price = 1
        try:
            for price in prices[idx + 1:]:
                if price >= prices[idx]:
                    idx_price += 1
                else:
                    break
            answer.append(idx_price)
        except:
            answer.append(0)
    answer.append(0)
    return answer
