from to_dict import Dictable

class B(Dictable):
    def __init__(self, val: int):
        self.val = val

class A(Dictable):
    def __init__(self):
        self.a = 5
        self.b = 'b'
        self.version2 = B(999)

print(A().dict)