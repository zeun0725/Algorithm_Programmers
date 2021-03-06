# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_book.sort()
    pre = phone_book.pop(0)
    while phone_book:
        for book in phone_book:
            if book.startswith(pre):
                return False
        pre = phone_book.pop(0)
    return True


def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    for idx, book in enumerate(phone_book):
        for other in phone_book[idx + 1:]:
            if other.startswith(book):
                return False
    return True