'''
use set, add, remove, random
'''

import random

class RandomizedSet:

    def __init__(self):
        self.random = set()

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random.add(val)
            print(True)
        print(False)
        
    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            print(True)
        print(False)
        
    def getRandom(self) -> int:
        value = random.choice(list(self.random))
        print(value)
