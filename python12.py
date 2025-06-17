# 1
name=input("enter  name :")
Class=input("enter class:")
section=input("enter section: ")

m=int(input("math: "))
e=int(input("english:"))
p=int(input("physics"))
c=int(input("chemistry"))
g=int(input("biology"))
result=(m+e+p+c+g)/5


print( "name:",name)
print("class:",Class)
print( "section:", section)
print( "result",result)

#2
a= int(input ("enter a :"))
b= int(input ("enter b :"))
c= int(input ("enter c :"))
sum = (a+b+c)
print("the sum is " , sum)


#3
s=int(input(" enter the value of  s :"))
square= s*s
print("the square is :" ,square)

#4
temp= str(input("enter the teamparature in celcius :"))
conv = float(temp)
fahr=((conv*9/5)+32)

print("the temperature in celcius is :",temp)
print("the temperature in fahrenheit", fahr)

#5
 
a=int( input("enter the a : "))
b=int(input("enter the b :"))
print(a//b)
print(a%b)