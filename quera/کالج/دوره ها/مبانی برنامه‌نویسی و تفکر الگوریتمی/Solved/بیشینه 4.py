a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b:
    a = b #now a is maximum of a,b
if a < c:
    a = c #now a is maximum of a,c,b
if a < d:
    a = d #now a is maximum of a,d,c,b
    
print(a)
