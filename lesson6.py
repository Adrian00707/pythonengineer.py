class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Child(Person):
    def __init__(self, name, age, location="Home"):
        super().__init__(name, age)
        self.location = location

    def set_location(self, new_location):
        self.location = new_location

    def display_location(self):
        print(f"{self.name} is currently at {self.location}")


class Bus:
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        print(f"{child.name} has been added to the bus.")

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            print(f"{child.name} has been removed from the bus.")
        else:
            print(f"{child.name} is not in the bus.")

    def change_location_for_all(self, new_location):
        for child in self.children:
            child.set_location(new_location)
        print(f"All children are now at {new_location}")

    def display_children(self):
        for child in self.children:
            child.display_location()


child1 = Child("Alice", 10)
child2 = Child("Bob", 9)
child3 = Child("Charlie", 8)


school_bus = Bus()


school_bus.add_child(child1)
school_bus.add_child(child2)


school_bus.display_children()


school_bus.change_location_for_all("School")


school_bus.display_children()


school_bus.remove_child(child1)

school_bus.display_children()


class Driver(Person):
    def __init__(self, name, age, bus):
        super().__init__(name, age)
        self.bus = bus

    def drive_to(self, location):
        print(f"Driver {self.name} is driving the bus to {location}.")
        self.bus.change_location_for_all(location)


driver = Driver("Mr. Smith", 45, school_bus)
driver.drive_to("Park")


class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(f"{self.name}, 'age': {self.age}, 'IsHappy':{self.isHappy}")


cat1 = Cat()
cat1.set_data('Bar', 4, True)
cat2 = Cat()
cat2.set_data('Popa', 1, False)


print(cat1.get_data())


class Building:

    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print(f"Year: {self.year}, City: {self.city}")


class School(Building):
    pupils = 0

    def __init__(self, year, city, pupils):
        self.pupils = pupils
        super().__init__(year, city)

    def fet_info(self):
        super().get_info()
        print(F"Pupils:{self.pupils}")

    pass


school = School(2000, 'Ing', 100)
school.fet_info()
