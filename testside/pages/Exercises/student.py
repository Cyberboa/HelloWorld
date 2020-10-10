class Student:
    # A class representing a student
    def __init__(self, name, ageX, address):
        self.full_name = name
        self.age = ageX
        self.address = address

    def get_age(self):
        return self.age


roshan = Student("Roshan Hausammann", 31, "Switzerland")

print(roshan.full_name, roshan.address)
print(roshan.get_age())
