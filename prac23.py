
  
print("Welcome to Coderail Railway Booking System")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Train Classes:\n first class \n second class \n sleeper class   ")
choice = int(input("Enter your choice : "))

if choice == 1:
    class_selected = "First Class"
    price = 1500
elif choice == 2:
    class_selected = "Second Class"
    price = 1000
elif choice == 3:
    class_selected = "Sleeper Class"
    price = 500
else:
    print("Invalid choice")
    class_selected = "None"
    price = 0


if age < 5:
    print("The ticket is free")
    price = 0
elif age > 60:
    print("20% senior citizen discount applied")
    price = price - (price * 0.20)


food = input("Do you want to add a meal? (yes/no): ").lower()

if food == "yes":
    print("Meal added")
    price += 200
else:
    print("No meal added")


print("----- Ticket Summary -----")
print("Name        :", name)
print("Age         :", age)
print("Class       :", class_selected)
print("Meal Added  :", "Yes" if food == "yes" else "No")
print("Total Price : ", price)






#2


print("welcoem to burger king")
print("1.  Whopper Burger : ₹150 \n 2. Crispy Veg  : ₹100  \n 3.Chicken Wings : ₹120  ")
choice =(int (input("enter your choice ")))
if choice==1:
    item="Whopper Burger "
    price=150
    
elif choice ==2:
    item=" Crispy veg "
    price=100
    
elif choice==3:
    item="Chicken Wings "
    price=120
   
quantity = int(input(" enter quantity :"))

coupon=input("do you have aby coupon code ? (yes/no)")

if coupon=="yes":
    a=input(" enter coupn :")

    if a=="KING50":
        discount=0.5
    elif a=="BK20  ":
        discount=0.2
    elif a =="NOCOUPON":
        discount=0

total_price = price * quantity
final_price=total_price-(total_price*discount)

print("----------BILL------------")
print("item :", item )
print("per item price :", price)
print("total price :", total_price )
print("final_prioce ", final_price)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
