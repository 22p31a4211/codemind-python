t=int(input())
a=[]
x=0
for i in range(t):
    a.append(input())
for i in a:
    if i=='X++' or i=='++X':
        x=x+1
    if i=='X--' or i=='--X':
        x=x-1
print(x)