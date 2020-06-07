from enum import Enum
import json

from to_dict import Dictable

class E(Enum):
    test = 'test_val'

class D:
    def __init__(self):
        self.val = 'str_val'

class C:
    def __init__(self):
        self.d1 = D()
        self.d2 = D()

class B(Dictable):
    def __init__(self, vals: list):
        self.vals = vals

class A(Dictable):
    def __init__(self):
        self.a = 5
        self.b = 'b'
        self.c = E.test
        self.d = C()
        self.e = [B([996, 997]), B([998, 999])]
        self.f = {'key_1': B([996, 997]), 'key_2': B([998, 999])}

print(A().dict)
print(json.dumps(A().json, indent=4))