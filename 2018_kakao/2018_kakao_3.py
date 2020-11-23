# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680#

import time
from collections import defaultdict

class Queue:
    def __init__(self, size):
        self.time = 0
        self.size = size
        self.queue = defaultdict(float)

    def insert(self, item):
        try:
            if not self.is_hit(item):
                if len(self.queue) == self.size:
                    self.delete()
                self.queue[item] = time.time()
                self.time += 5
            else:
                self.time += 1
        except: #self.size = 0 일때
            self.time += 5

    def is_hit(self, item):
        if item in self.queue.keys():
            self.queue[item] = time.time()
            return True
        return False

    def delete(self):
        del self.queue[sorted(self.queue.items(), key=lambda x: x[1])[0][0]]

    def get_time(self):
        return self.time


def solution(cacheSize, cities):
    cache_queue = Queue(cacheSize)
    for city in cities:
        cache_queue.insert(city.lower())
    return cache_queue.get_time()