#1
n=int(input("enter the number of entries : "))
d={ input("enter key :"):  input("enter value: " ) for i in range(n)}
print(d)


#2

employee_details={1:{'name':'rahul', 'department':'business','salary':50000}, 
                  2:{'name':'rohan', 'department':'hr' , 'salary':100000 },
                  3:{'name':'roshani', 'department':'project managing' , 'salary':70000 },
                  4:{'name':'rohan', 'department':'tachnical' , 'salary':60000 },}

high_salary=[u['name'] for u in employee_details.values() if u['salary']>50000]
print(high_salary)     
        
        
#3
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


#4
amount = int (input("enter the amount : "))
if amount>1000:
        disc=0.12*amount
elif 500<amount<1000:
        disc=0.05*amount
else:
        print("no discount")
print("the discount is : " , disc)
#5
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

#6

li = [20, 30, 40, [57, 66, 30, [70, 80], "Hello"], 50, True]


inner_list = li[3][3]
a= inner_list.index(80)
inner_list.insert(a, 76)


outer_list = li[3]
b = outer_list.index(57)
outer_list.insert(b + 1, 88)
print("modified list :" , li)

h_letter=li[3][5][0]
print("H letter :" , h_letter)      
        
        
#7
print("welcome to the trip planner") 
budget=int(input("please enter yopur budget : 50000-10000,10000-20000,20000-30000,30000-40000 :  ")) 
if budget>5000 and budget < 10000:
    countries=["shrilanka","bhutan","nepal"]
elif budget>10000 and budget <20000:
    countries=["singpore","malisha","thiland"]     
elif budget>20000 and budget <30000:
     countries=["Qatar","Hongkong","Vietnam"]
elif budget >30000 and budget<40000:
     countries=["South Korea","China","Canada"]
else:
    print("sorry no pacakge under thsi budget ")

if countries :
    print(" countreis available under this budget are: ")
    for i in countries :
        print(i)  
choice=input("select your choice : ")
places={
    "shrilanka":"temple of tooth Relic ",
    "bhutan":" Takin Zoo",
    "nepal":"Devi Falls",
    "singapore":"Dolphin Lagoon",
    "malisha":"Kuala Lumpur",
    "thiland":"elephant show ",
    "Qatar":"Doha",
    "Hongkong":"Lantau Island",
    "Vitenam":"Ha Long Bay",
    "South Korea":"Seol",
    "China":"Beijing’s Great Wall",
    "Canada":"Niagara Falls",
}
if choice in places:
    print(f"the places to visit in {choice} is {places[choice]}")
else:
    print("invalid country selected")
        
        
        
