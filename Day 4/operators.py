print("------------------Operators--------------------")

x, y, z = 100, 200, 300
lst = [10, 20, 30, 40, 'Hello', 'Kamiyab']
print("x:",x)
print("y:",y)
print('z:',z)
print("lst:",lst)
print("-----------------------------------------------")

#arithmetic operators
print("<-----Arithmetic operators----->")
print(f'Summation of {x} and {y}: {x+y}')
print(f'Subtraction of {x} and {y}: {x-y}')
print(f'Multiplication of {x} and {y}: {x*y}')
print(f'Division of {x} and {y}: {x/y}')
print(f'Floor Division of {x} and {y}: {x//y}')
print(f'Modulus of {x} and {y}: {x%y}')

#comparison operators
print("<-----Comparison Operators----->")
print(f"{x}>{y}: {x > y}")
print(f"{x}<{y}: {x < y}")
print(f"{x}=={y}: {x ==y}")
print(f"{x}>={y}: {x >= y}")
print(f"{x}<={y}: {x <= y}")
print(f"{x}!={y}: {x != y}")

#logical operators
print("<----Logical Operators---->")
#and operator
print("-----and operator-----")
if x>y and x>z:
    print(f"{x} is the largest")
if y>x and y>z:
    print(f"{y} is the largest")
if(z>x and z>y):
    print(f"{z} is the largest")
#or operator
print("----or operator----")
ch=input("enter char:")
if(ch=='A'or ch=='a'or ch=='E'or ch=='e'or ch=='I'or ch=='i' or ch=='O'or ch=='o'or ch=='U'or ch=='u'):
    print(ch," is Vowel")
else:
    print(ch," is not Vowel")

#membership operators
print("<----Membership Opearators---->")
print("x in lst:", x in lst)
print("y in lst:", y in lst)
print("y not in lst:", y not in lst)

#identity operators
print("<----Identity Opearators---->")
print("x is y:", x is y)
print("x is not y:", x is not y)