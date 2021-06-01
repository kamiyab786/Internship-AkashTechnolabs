'''
Create a class cal4 that will calculate square of a number. Create
setdata() method which has one parameters that contain number.
Create display() method that will calculate sum.(Function should
return value)'''
import math


class Cal4:
    def setdata(self, num):
        self.num = num

    def display(self):
        square = self.num ** 2
        return square


obj = Cal4()
value = int(input("Enter any number:"))
obj.setdata(value)
print(f'Square of {value} = {obj.display()}')