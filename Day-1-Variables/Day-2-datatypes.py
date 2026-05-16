''' 
data types in python
1.mutable => can be changed after creation => list,dict,set,bytearray
2.immutable => can not be changed after creation =>int,float,bool,tuple,frozenset,bytes,string

'''

#integer =>  stores whole numbers
num = 2
x=-2
print(type(x))

#float =>  stores decimal values =>immutable
num_2=3.14
print(type(num_2))

# string =>  stores text data =>immutable
string_1 ="bhoomi"
print(type(string_1))
print(string_1[0]) #access character

# boolean =>it stores only true or false 
is_student = True
is_logged_in = False

# list =>mutable
nums=[1,2,3]
nums[0]=100 # changed after creation 
print(nums)

nums_1 = ["bhoomi", True,4.3] #list with diff data types


# tuple => a tuple stores multiple values but tuple cannot be changed
#immutable
data = (1,2,3)
print(data)
data_2 =("bhoomi", 21, True ) # it is possible to have different datatypes in tuple

# dictionary(dict) => a dictionary stores key value pairs it is similar to objects in java script
student={
"name":"Bhoomi"
}
print(student["name"])
student["age"] = 21 #adding a value 
print(student)

 # set => a set is a collection that stores unique values only it remove duplicates automatically =>mutable 
numbers = { 1,2,3,4}
print(numbers)

numbers_2={ 1,1,2,3,4,4,5,5}
print(numbers_2)
numbers_2.add(8) #.add is only for set to adding values
print(numbers_2)



