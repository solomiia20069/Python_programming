from errors import MaxStudentsError

class Group:
    MAX_STUDENTS = 10
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise MaxStudentsError()
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