#create a function that checks weather a number is even or odd
def calculate( number ):
    if number%2==0:
        return "number is even"
    else:
        return "number is odd"
    
number = int(input("enter ur number "))
print(calculate(number))

#write a function that return the greater number 
def greater(a,b,c):
    if a>b and a>c:
        return "a is greater"
    if b>a and b>c:
        return "b is greater"
    else:
        return"c is greater"
    
a = int(input("enter ur a" ))
b = int(input("enter ur b" ))
c = int(input("enter ur c" ))
print(greater(a,b,c))

#make a function for conversion from celsius to ferhanite
def convert(c):
    f = (5/9)*c+32
    return f
c=float(input("enter c"))
print("temperaature is in ferhanite",convert(c))

#write a function to find area of circle
def area(radius):
    area = 3.14*radius**2
    return area

radius = float(input("enter ur radius "))
print("area of circle is ", area(radius))

#factorial using function
def fact(number):
    fact=1
    for i in range (number,1,-1): 
     fact = fact*i
    return fact
number = int(input("enter ur number "))
print(fact(number))

#write a function to check prime number
def prime(number):
 if number <=1:
  return"not prime"
 
 for i in range ( 2,number):
    if number % i ==0:
       return "not prime "
   
 return "prime"
print(prime(10))
  
