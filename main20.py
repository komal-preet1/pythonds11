#1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#2
n = int(input("Enter number: "))
is_prime = True

if n <= 1:
    print("The number is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
           

    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")
        
#3
marks=int(input("enter marks between 0 and 100"))
if marks>100 :
    print("sorry marks are out of range ")
elif 90<=marks < 100:
    print("GRADE:A")
elif 80<=marks < 89:
    print("GRADE:B")
elif 70<=marks < 79:
    print("GRADE:C")
elif 60<=marks <69 :
    print("GRADE:D")
elif  marks<60 :
    print("GRADE:F")

#4
a=int(input("enter the number "))
for i in range(1,11):
    print(a , " *" , i ," = " , a*i)

#5
b=[]
u=[i*i for i in range(1,20) if i%2==0]
b.append(u)
print(b)

#6
n=int(input("enter the year"))
if ( n%4==0 and n%100!=0) or (n%400==0):
    print("leap year")
else:
    print("not leap year")

#7
a=int(input("enter the side A :"))
b=int(input("enter the side B  :"))
c=int(input("entye rthe side C :"))

if (a+b>c and b+c>a and c+a>b):
    print("the triangle is valid")
    if a==b==c:
        print("the triangle is equilateral ")
    elif a==b or a==c or b==c:
        print("the triangle is issoceles ")    
    elif a**2+b**2==c**2 or a**2+c**2==b**2  or b**2+c**2==a**2:
        print("the triangkle is equilateral")
    else:
        print("scalene triangle")   
        
#8
a=int(input("Enter  the  number :"))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
elif a==0:
    print("the number is zero ") 

#9
password = input("Enter your password: ")


has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_+=<>?/"


for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters.")
elif not has_upper:
    print("Password must contain at least one uppercase letter.")
elif not has_lower:
    print("Password must contain at least one lowercase letter.")
elif not has_digit:
    print("Password must contain at least one digit.")
elif not has_special:
    print("Password must contain at least one special character (!@#$%^&*()-_+=<>?/).")
else:
    print("Password is strong!")




#!0
w=float(input("enter your weight : "))
h=float(input("enter your height in m  "))
bmi=w/(h*h)
print (f" the weight in bmi is {bmi}")
if bmi<18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9: 
    print("Normal weight")
elif 25 <= bmi < 29.9: 
    print("Overweight")
elif bmi >= 30: 
    print("obesity")
  

#11
choice= int(input("entee the number of day "))
if choice==1:
    print("sunday")
elif choice==2:
    print("monday")
elif choice==3:
    print("tuesday")
elif choice ==4:
    print("wednesday")
elif choice==5:
    print("thursday")
elif choice==6:
    print("friday")
elif choice==7:
    print("saturday")
else:
    print("not a day")

#12

amount = int (input("enter the amount : "))
if amount>1000:
        disc=0.12*amount
elif 500<amount<1000:
        disc=0.05*amount
else:
        print("no discount")
print("the discount is : " , disc)



#13
n=int(input("enter the number till you want to have sum :"))
sum=0
for i in range (1,n+1):
    sum=sum+i
print("the sum is:",sum)


#14
employee_details={1:{'name':'rohan', 'department ': 'hr' , 'salary':30000},
                  2:{'name':'roshan','department':'project manager', 'salary':55000},
                  3:{'name':'priya','departmnet':'business', 'salary': 65000},
                  }
high_salary=[u['name'] for u in employee_details.values() if u['salary']>50000]
print(high_salary)


#15
from collections import Counter
str="hey there today is sunday "
v="AEIOUaeiou"
cnt=Counter([i for i in str if i in v])
print (cnt)



#16



num = int(input("Enter a number: "))


sum_of_digits = 0


while num > 0:
    digit = num % 10        # Get the last digit
    sum_of_digits += digit  # Add it to the sum
    num = num // 10         # Remove the last digit


print("Sum of digits:", sum_of_digits)



#17

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(i):     
        print("*", end="")
    print()  
    
#18
import random
a=int (input("enter the number between 1 and 100 :"))
low=0
high=0
random_number=random.randint(0,100)
print(f"the random number is {random_number}")
if a> random_number :
    print("too high !!")
elif a<random_number:
    print("too low")
else:
    print("corrected ")

#19
n=int(input("enter the number :"))
for  i in range (1,n+1):
    if i%2==0:
        print("even number is  ",i)

#20
list = [12, 25, 34, 25, 19, 8, 25, 16, 40, 33]
if 25 in list:
    print("25 exixts in list ")
else:
    print(" 25 is not present in this list ")
print("the length of list ", len(list))
print("number of occurrneces of 25 " , list.count(25))
print("traversing of each elemnent :")
for num in list:
    print(num, end=" ")
    print()
even_numbers=[i for i in list if i%2==0]
print(even_numbers)

#21
a = input("Enter string: ")
words = a.split()

if len(words) < 10 or len(words) > 19:
    print(" The string is not valid (should be 10 to 19 words).")
else:
    print("The string is valid.")


    if words == words[::-1]:
        print(" The string is a palindrome (word-wise).")
    else:
        print(" The string is not a palindrome.")


    mid_index = len(words) // 2
    print("3. Middle word in the string:", words[mid_index])


    print("4. Second last word in the string:", words[-2])


#22
print("Welcome to calculator")
choice=int(input("enter your choice: "))
a=int(input("enter first number: "))
b=int(input("enter  second number :"))
if choice==1:
    sum=a+b
    print("sum is ",sum)
elif choice==2:
    subs=a-b
    print("substraction is " , subs)
elif choice==3:
    mul=a*b
    print("multiplication is " ,mul)
elif choice==4:
    div=a/b
    print("division is ", div)    
else:
    print("not accurate choice")
 
#23

strings = ['abc', 'xyz', 'aba', '1221','xys','xyx']


count = 0

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of matching strings:", count)
