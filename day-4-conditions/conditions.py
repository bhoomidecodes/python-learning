#if statement
age = 20
if age>20: # it will run if condition will be true
 print("adult")

#  if else statement => true than if otherwise else 
number = 7
if number%2==0:
  print("even")
else:
  print("odd")

 # if-elif- else statement =>it will check multiple conditions         
  marks = 85
  if marks>=90:
    print("grade A")
  elif marks >= 70:
    print("grade b")
  else:
    print("grade c")
  
#nested if 
age = 20
has_id = True
if age >= 18: 
  if has_id ==True: # this if will only execute if upper if willbe true
   print("entry allowed")

#nested if else =>  indentation same mean same block / same pair
age = 20
has_id==True
if age>=18: #outer if
  if has_id==True: #inner if 
    print("entry allowed")
  else:
    print("id required") # inner if ka else 
else:
 print("underage") #outer if ka else

#if with and => both conditions should be true
username ="admin"
password = "12345"
if username == "admin"and password=="12345":
  print("login successful")
  
# if with  or => if even one condition is true than it will work
day ="sunday"
if day=="sunday"or day=='saturday':
  print("holiday")

  #if with not => it will make the condition opposite
  logged_in=False
  if not logged_in:
    print("please login first")


  
