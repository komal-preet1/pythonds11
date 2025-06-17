#1

l1 = 'hello today is a rainy day'

l2 = l1.split()

result = [i for i in l2 if len(i) <4]
print(result)


#2

l2=['even' if i%2==0 else 'odd' for i in range(0,20)]
print(l2)


#3

l3=[i for i in range (1,1000) if i%7==0 ]
print(l3)

#4
a='hello this is the python with data science class'
b=len([i for i in a if i ==' '])
print(b)





#5
a=[1,2,3,4]
b=[2,3,4,5]
c=[i for i in a for j in b if i==j]
print(c)