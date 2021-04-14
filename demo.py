from jsoncodable import JSONCodable

class BirthDay(JSONCodable):
    def __init__(
        self,
        month: int,
        day: int
    ):
        self.month = month
        self.day = day

class Person(JSONCodable):
    def __init__(
        self,
        name: str,
        birth_month: int,
        birth_day: int
    ):
        self.name = name
        self.birth_day = BirthDay(birth_month, birth_day)

person = Person(
    name='John',
    birth_month=7,
    birth_day=7
)


person.jsonprint()

# prints
#
# {
#     "name": "John",
#     "birth_day": {
#         "month": 7,
#         "day": 7
#     }
# }


Person.load(person.json).jsonprint()

# prints
#
# {
#     "name": "John",
#     "birth_day": {
#         "month": 7,
#         "day": 7
#     }
# }