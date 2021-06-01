'''
. Create a class cal5 that will calculate area of a rectangle. Create
constructor method which has two parameters .Create calArea()
method that will calculate area of a rectangle. Create display() method
that will display area of a rectangle
'''


class Cal5:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calArea(self):
        self.area = self.length * self.width

    def display(self):
        print(f'Area of rectangle with length({self.length}) and width({self.width}) = {self.area}')


length = int(input("Enter length: "))
width = int(input("Enter width: "))

obj = Cal5(length, width)
obj.calArea()
obj.display()