# write a function to add two numbers 
def add( num1,num2):
    return num1+num2

print(add(1,1))

#write a function to find square
def square (number):
    return number ** 2
n= int (input("enter  a number "))
print(square(n))

#write a function to multiply 
def multiply(a,b):
    return a*b

a=int(input("enter a "))
b = int(input("enter b"))
print(multiply(a,b))

#create a functin that return both area and circumference of a circle given its radius
def circle(radius):
    area = 3.14 * radius*radius
    circumference = 2*3.14*radius
    return area,circumference

r = float(input("enter radius "))
a,c = circle(r)

print ("area",a)
print ("circumference",c)

#greet user
def greet(name="user"):
    return "hello,"+name+"!"
print(greet("bhoomi"))

#create a lamda function to compute the cube of a number
cube = lambda x:x**3
print(cube(3))

