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

# Save with gzip
gzip_file_path = 'test.json'
patched_gzip_file_path = person.save(gzip_file_path, gzipped=True)
# returns a file_path which has a '.gz' extension if not present at the end of your provided path
# also prints a message to let you know, that the path had been modified

Person.load(patched_gzip_file_path).jsonprint()

# prints
#
# {
#     "name": "John",
#     "birth_day": {
#         "month": 7,
#         "day": 7
#     }
# }


# Cleaning up

import os

os.remove(patched_gzip_file_path)