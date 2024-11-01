class Persons:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def show_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
