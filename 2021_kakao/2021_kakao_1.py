# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
import re
def solution(new_id):
    new_id = new_id.lower()
    _new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    _new_id = re.sub('\.{2,}', '.', _new_id)
    _new_id = _new_id.strip('.')
    if not _new_id:
        _new_id = 'a'
    _new_id = _new_id[:15]
    _new_id = _new_id.strip('.')
    while _new_id.__len__() <= 2:
        _new_id = _new_id + _new_id[-1]
    return _new_id

