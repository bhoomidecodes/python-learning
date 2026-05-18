#loops => for loop , while loop
#for loop is used when we know that how man y times the loop will run
for i in range(19):
 print(i)
 
 #range(start,stop,step)
for i in range(0,10,2):
 print(i)

for i in range(1,10):
 print(i)

for i in range( 1,10):
  print("b2","c3","c3")

  #print even number  from 1 to 20 
  for i in range ( 2,22,2):
   print(i)

#print table of 5
for i in range ( 1,11):
 print("5*",i, "=",5*i)

#print any table
num =int(input("enter ur num "))
for i in range ( 1,11):
  print(num ," x " ,i , "=", num * i)

#print number form 10 to 1 
for i in range ( 10 , 1,-1):
 print (i)

#print all even numbers from 1 to 50
for i in range ( 2,50,2):
 print(i)

 #Print all odd numbers from 1 to 50.
 for n in range ( 1 , 50 ,2):
  print(n)

  #print multiplication table of 7
 
for i in range (1,11): # in python last range() no. is not include so we are taking 11 here for printing upto 10
   print("7x",i,"=", 7*i )

sum = 0
for i in range ( 1,101):
   sum = sum+i
   print (  sum) # it will give values of every iteration
print(sum) # it will give the final value after addition

#factorial of n number 
num = int(input("enter ur number"))
fact = 1 
for i in range(num,1,-1 ):
   fact = fact*i

print(fact)

#count how many numbers =>by while loop
num = 123
count = 0
while num !=0:
   num//=10 # num = num//10
   count +=1 # count = count+1

print("number of digit ",count)

# by len()function =>after converting it into string
num = 123456
print( "no. of digits = ", len(str(num)))

name = "bhoomi sharma"
for i in name:
  print(i)

#while loop => continues to execute as long as the condition is true
count = 0 
while count<5:
  print(count)
  count=count+1
  
#loop control statements 
#1.break=> the break statement  exists the loop permaturely 
for i in range ( 10):
  if i ==5:
    break
  print(i)

#continue=>the continue statement skips the current iteration and continue with the next
for i in range (10):
  if i%2==0:
    continue
  print(i)

#pass=> its a null operation nd does nothing
for i in range (5):
  if i ==3:
    pass
  print(i)

  #nested loop
  for i in range(3):
    for j in range(2):
      print (f"i:{1}and j:{j}")

      
