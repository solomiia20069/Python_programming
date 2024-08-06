MAX_STUDENT_NUM = ("The group can't contain more than 10 students", 400)
            #write all types of errors here and just call them below

class MaxStudentsError(Exception):
    def __init__(self, message=MAX_STUDENT_NUM):
        self.message = message
        super().__init__(self.message)

