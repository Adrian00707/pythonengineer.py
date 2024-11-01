from persons import Persons


class Student(Persons):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def show_info(self):
        super().show_info()
        print(f"Student id: {self.__student_id}")
