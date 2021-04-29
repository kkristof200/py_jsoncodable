from jsoncodable import JSONCodable, CompressionAlgorithm

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

import os

# Save with compression
json_file_path = 'test.json'

for c in CompressionAlgorithm:
    compressed_file_path = person.save(json_file_path, compression=c)
    # returns a file path which has the compressed extension if not present at the end of your provided path
    # also prints a message to let you know, that the path had been modified


    Person.load(compressed_file_path).jsonprint()
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

    os.remove(compressed_file_path)