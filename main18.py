#1
a=(1,2,4,52,1,2,3)
a=set(a)
print(a)
b=tuple(a)
print(b)


#2
a=[[1,2],[3,4],[5,6]]
b=[]
for i in a :
    for j in i:
        b.append(j)
print(b)
        

#3
l=(3,5,1,8,2)
k=(max(l))
m=(min(l))
print('the maximum value is ' , k, 'the minimum value is ' , m)

#4
t=(1,2,3,4,5)
u=[i*i*i for i in t  ]
print(u)
res= list(zip(t,u))
print(res)
    