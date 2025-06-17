#question 1
number=int(input("enter a number between 1 to 12 "))
if number==1 :
  print ("january")
elif number==2 :
    print("february")
elif number==3 :
    print("march")
elif number ==4 :
    print("april")
elif number ==5 :
    print("may")
elif number ==6 :
    print("june")
elif number ==7:
    print("july")
elif number==8:
    print("august")
elif number==9:
    print("september")
elif number==10:
    print("october")
elif number ==11 :
    print("november")
elif number==12 :
    print("december")
else:
    print("enter valid number")

#question2
num1=int(input("enter number :"))
num2 = int (input ("enter number :"))
firstname = input("enter first name : ") 
lastname = input ("enter lats name: ")
if num1==num2 :
    print ("both numbers are equal")

elif num1>num2 :
    print("num1 is greater")
    for i in range (5):
        print(firstname)
elif num1<num2:
    print("num2 is greater")
    
    for j in range (3):
         print(lastname)
else :
    print("invalid")
if num1<=num2:
   print("num1 is smaller or equal to num 2")
else:
    print("num 1 is greater")
    
    
#question 3
str1=input("enter first string ")
str2=input("enter seconmd string ")
if (str1==str2): 
    print("both strings are equal")
else :
     print("not equal")
 
print(str1 is str2)


#question 4
a=str(input("enter string: "))
b=str(input("enter string: "))
a=int(a)
b=int(b)
print(type(a))


print(a is b)


# question 5
num = int(input("Enter a number: "))

total = 0
for i in range(1, num + 1):
    total += i
print("The sum of numbers from 1 to", num, "is:", total)


# question 6
num=int(input("enter number : "))

for i in range (0,num):
    if i%2==0:
      print( i)
      
      

# question 7
n=int(input("enter number"))
for i in range (0,n,1):
    print(i)
for j in range (n,0,-1):
    print(j)
      
      
# question 8
num=int(input("enter number"))

for i in range (0,11):
    
      print( i*num)
      

#question 9
for i in range(4):
    for j in range(0,i+1):
       print (j+1 , end=" ")
    print()
    
    
# question10
N = int(input("Enter the value of N: "))
for i in range(1, N + 1):
    print(i**2)
    
