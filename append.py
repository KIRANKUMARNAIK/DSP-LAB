#appending of two lists
a=[6,7,8,9,10]
b=[1,2,3,4,5]
c=[3,-4,-6,-8,3,4,-10]
d=[1,3,4,5,6,9,7]
print("the three pre defined lists are:")
print("list a:"),a,("\nlist b:"),b,("\nlist c:"),c,("\nlist d:"),d
for i in range(0,len(a)):
	b.append(a[i])
print("the new list after appending is:\n"),b
for i in range(0,len(c)):
	if(c[i]<0):
        	a.append(c[i])
print("appending of only negative numbers of list c to list a is:\n"),a
for i in range(0,len(d)):
	if(d[i]%2==0):
		c.append(d[i])
print("appending of only even numbers of list d to list c is:\n"),c

