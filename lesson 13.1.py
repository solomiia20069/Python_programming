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
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if student not in self.group:
            self.group.append(student)

    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.group.remove(student)

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"

# Example usage
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')

