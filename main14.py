  
    
 #1
str1='coder'
str2='roots'
str3=str1[:2]+str2[-2:]
print(str3)
str4='new'
str5='year'
str6=str4[:2]+str5[-2:]
print(str6)
#2



str1="coder"
str2="roots"
a=str1.replace("c","r")
b=str2.replace("r","c")
print(a + " " + b)


#3
str1=input("enter string :")
str2="ing"
str3="ly"
if len(str1)<3:
    print(str1)
else:
    print(str1+str2)
    
if str1.endswith("ing"):
    print(str1+str3)
else:
    print(str1)
    
    
#4



string = input("Enter a  string: ")
n = int(input("Enter the index : "))
if n < 0 or n >= len(string):
    print("Index out of range")
else:
    
    modified_string = string[:n] + string[n+1:]
    print("Original String:", string)
    print("Modified String:", modified_string)
