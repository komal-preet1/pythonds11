#1

l1=[2,3,4,5,1,6,7,8,9,0]
print(l1)


#2
l2=[1,10,100,3,6,8]
print(l2)
l2.insert(2,59)
print(l2)
l2.append(5)
print(l2)
print(len(l2))


#3
l3=[1,4,2,42,4,6,2,56,4,56,2]
for i in range(0,len(l3),2):
   
       print(l3[i])

#4,5
l4=["gaurav",12,23,33.33,"sharma",True]
print(l4[0:len(l4):4])
y=(l4[1:4])
print(y)
for i in y:
    i+=i
print(i)


#6


a=["rahul","rajni","kamal","pooja"]
b=input("add friend name :")
a.append(b)
print(a)

c=input("enter the most imporatnat friend name ")
d=int(input("enter the loaction at whoch youy wnat to add"))
a.insert(d,c)
print(a)7