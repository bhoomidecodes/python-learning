 #tuples are ordered collection of itmes that are immutable . they are similar to lists , but their immutability makes them different
#it allows duplicates

empty_tuple =()
print(empty_tuple)
print(type(empty_tuple))

#list = print(type(list())) #empty list 
list_01 = list((1,2,3,4,5)) #converting tuple into list
print(list_01)
print(type(list_01))

numbers = tuple([1,2,3,4,5,6]) #tuple() is a build in function that convert the iterable in tuple
print(type(numbers))

mixed_tuple = ( "heloo",2,"true",0.1)
print(mixed_tuple)

#accessing tuple elements
print(numbers[0])
print(numbers[2])

print(numbers[0:4])

#tuples operations
print(numbers+mixed_tuple)

#single element tuple
single = (5,)#comma is mandotary otherwise it will give int output
print(type(single))

#string tuple
letters = tuple("hello")
print(letters)

#negative indexing 
print(numbers[-1])

#slicing
nums = (1,2,3,4,5)
print(nums[1:4])

#tuples operations => 1. concatenation 
a = (1,2)
b=(3,4)
print(a+b)

# 2. repetition
a=(2,3)
b = (3,4)
print((a,b)*3)
print((2,3)*3)

#tuples methods 

#tuples only have 2 built in methods because they are immutable 
#so they dont have modification methods like lists

#1.count
nums =(1,1,2,3,3,4)
print(nums.count(1))

# 2. index()
nums = (10,20,30)
print(nums.index(20))

