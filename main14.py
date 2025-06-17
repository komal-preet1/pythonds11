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
    
    
    
    
    
 
   
    
#2
str3="coder roots"
swapped_name= str3.split()[-1] + " " +str3.split()[0]
print(swapped_name)


str1="coder"
str2="roots"
print(str1.replace("c","r"))
print(str2.replace("r","c"))
str3=str1+str2
print(str3.replace("c ", "r") and str3.replace("r","c"))
print(str3)