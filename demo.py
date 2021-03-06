from jsoncodable import JSONCodable
import json

class Test1:
    def __init__(self, value: int):
        self.value1 = value
        self.value2 = value * 2
        self.values = [self.value1, self.value2]

class Test2(JSONCodable):
    def __init__(self, value: int):
        self.test1 = Test1(value)

test2 = Test2(5)
print(test2.dict)
# prints:
# 
# {'test1': <__main__.Test1 object at 0x1018199d0>}

# print(json.dumps(test2.json, indent=4))
# or
test2.jsonprint()
#
# both will print:
# 
# {
#     "test1": {
#         "value1": 5,
#         "value2": 10,
#         "values": [
#             5,
#             10
#         ]
#     }
# }


class Test3(JSONCodable):
    pass

json_str = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

print(Test3.from_json(json_str))
print(Test3.from_json(json_str).hometown)
# prints:
# 
# JSONCodable(name='John Smith', hometown=JSONCodable(name='New York', id=123))

print(Test3.from_json(json.loads(json_str)))
# prints:
# 
# JSONCodable(name='John Smith', hometown=JSONCodable(name='New York', id=123))