fruits =[ "apple","banana","mango","papaya"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[4])

print(fruits[1:3]) #here ending index not including

#modifying the list element
fruits[1]="watermelon"
print(fruits)

##list methods
fruits.append("orange") #add an item to the end
fruits.insert(3,"banana")  #add banana at index 3
print(fruits)
fruits.remove("banana") # it removes specific value
fruits.pop(1) #it removes using index

numbers =[ 3,4,2,9,-1]
numbers.sort() #arrange the list in ascending order
print(numbers)

number = [ 1,2,3,4,5]
number.reverse() #it will reverse the list
print(number)

number = [1,2,2,3]
number.count(2) #it will count that hw many times the value appear
print(number.count(2))

names = [ "riya","tiya","supriya"]
print(names.index("supriya")) #find index position of a value

a=[1,2]
b=[3,4]
a.extend(b) #add another list into current list
print(a) 

names =[ "neha","rohan"]
names.clear() #remove all elements from the list
print(names)

teas=["green tea","black tea","oolong tea"]
print(teas)
print(teas.copy()) #it will make a copy of list

