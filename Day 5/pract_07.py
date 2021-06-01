'''
Create a class cal6 that will calculate area of a square. Create setdata()
method that should take length from the user. Create area() method
that will calculate area . Create display() method that will display area .
'''


class Cal6:
    def setdata(self, length):
        self.length = length

    def area(self):
        self.area = self.length * self.length

    def display(self):
        print(f'Area of square with length({self.length}) = {self.area}')


obj = Cal6()
length = int(input("Enter length:"))
obj.setdata(length=length)
obj.area()
obj.display()