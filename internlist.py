#Create a list and print first and last element.
l=[]
n=int(input("Enter the number of elements to be inputed: "))
for i in range(n):
    s=int(input("Enter the elements: "))
    l=l+s
print("The first Character is:",l[0],"\n The last Character is:",l[n-1])

#Add and remove elements from a list.
m=[]
a=int(input("Enter the number of elements to be inputed: "))
for i in range(a):
    s=int(input("Enter the elements: "))
    m=m+s
b=int(input("Enter the element to be removed: "))
m.remove(b)
print(m)
c=int(input("Enter the element to be added: "))
m=m+c
print(m)

#Find maximum and minimum in a list.
k=[]
d=int(input("Enter the number of elements to be inputed: "))
for i in range(d):
    r=int(input("Enter the elements: "))
    k=k+r
print("Maximum in list is: ",max(k))
print("Minimum in list is: ",min(k))

#Reverse a list.
li=[]
nn=int(input("Enter the number of elements to be inputed: "))
for ii in range(nn):
    ss=int(input("Enter the elements: "))
    li=li+ss
newli=li[::-1]
print("Reversed List is: ",newli)

#Sort a list in ascending and descending order.
nlist=[]
nm=int(input("Enter the number of elements to be inputed: "))
for ij in range(nm):
    stn=int(input("Enter the elements: "))
    nlist=nlist+stn
nlistas=nlist.sort()
nlistds=nlist.sort(reverse=True)
print(nlistas)
print(nlistds)

#Count occurrences of an element.
cl=[]
nv=int(input("Enter the number of elements to be inputed: "))
count=0
for oi in range(nv):
    st3=int(input("Enter the elements: "))
    cl=cl+st3
cha=int(input("Enter the element whose frequency is to be found: "))
for z in cl:
    if z==cha:
        count=count+1
print("The occurence of the element is: ",count)

#Merge two lists.
f=[]
u=int(input("Enter the elements of the list: "))
for x in range(u):
    q=int(input("Enter the element: "))
    f=f+q
e=[]
w=int(input("Enter the elements of the list: "))
for y in range(w):
    p=int(input("Enter the element: "))
    e=e+p
print(f.extend(e))

#Remove duplicates from a list.

#Find second largest element in a list.

#Split list into even and odd numbers.
