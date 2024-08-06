class Human:
    def __init__(self, gender, age, name, surname):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}, Gender: {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)            self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))