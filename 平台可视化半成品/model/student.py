class Student:
    def __init__(self, stuInfo):
        self.header = ["student_id", "name", "gender", "phone_number", "email", "password", "grade", "college_id"]
        info = tuple(str(item) for item in stuInfo)
        self.info = dict(zip(self.header, info))
        print(self.info)
