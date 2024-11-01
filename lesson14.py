from datetime import datetime


def filter_and_square(numbers):
    result = []
    for n in numbers:
        if n > 10:
            result.append(n**2)
    return result


numbers = [4, 12, 5, 19, 7, 25]
result = filter_and_square(numbers)
print(result)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_p(self):
        return 2 * (self.a + self.b)


rect = Rectangle(5, 3)
print(f"Area: {rect.get_area()}")
print(f"Perimetr: {rect.get_p()}")


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


square = Square(4)
print(f"A: {square.get_area()}, P: {square.get_p()}")


try:
    print(5/0)
except ZeroDivisionError:
    print('Zero divided')

print(datetime.now().hour)
