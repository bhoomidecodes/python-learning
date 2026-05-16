# # taking input from user
# name=input("enter your name") #input will always return a string
# print(name) 
# print(type(name))

# #conversion => int(),float(),str(),bool()
# age=int(input("age"))
# print(type(age))

x=10
print(int(x))
print(float(x))

#operators in python => arthmetic operators
a= 10
b=20
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #remainder
print(a**b) #power
print(a//b) #floor division

# comparison operators (relational operators)
a=6
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

# assignment operators => used to assign nd update value

x= 10
print(x)

y=1
y+=11 #add nd assign
print(y)

z=10
z-=4 #subtract and assigns
print(z)

n=2
n*=3 #multiply and assign
print(n)

u=20
u/=4 #divide and assign
print(u)

w = 10
w%=3 #modulus and assign
print(w)

k=2
k **=3 #power and assign
print(k)

c = 10
c//= 3 #floor division assign
print(c)

#logical operators  and,or,not
age = 20
print(age>18 and age<25)  #both condition should be true then answer will be true

#if one condition will be true than answer will be tue
print(5>10 or 5>2) 

#not operator converts true-->false , false---->true
print(not True)


#membership operator
name="bhoomi" #in will check if the value is present
print("b" in name)
print("z" not in name)

#it will check if the object is sharing same memory location
a=[1,2]
b=a
print (a is b)

x=5
y=10
print(x is not y )

a = input("enter first number ")
b = input("enter second number")
c = input("enter third number")

if a>=b and a>=c:
    print("a is greater" , a)
elif b>=a and b >=c:
    print("b is larger" , b)
else:
    print("c is greater ", c)
