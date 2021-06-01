'''
Consider an employee class, which contains fields such as name and
designation. And a subclass, which contains a field salary. Write a
program for inheriting this relation.
'''

class Employee:
    name = "KAMIYAB"
    designation = "HR Manager"
    def display(self):
        print('Name : ', self.name)
        print('Designation : ', self.designation)

class Subclass(Employee):
    salary = 10000
    def display(self):
        print('Name : ', self.name)
        print('Designation : ', self.designation)
        print('Salary : ', self.salary)


obj1 = Employee()
obj2 = Subclass()
print('-------Employee class display()-------')
obj1.display()
print("-------Subclass display()---------")
obj2.display()