s=input()
r=l=u=d=0
for i in s:
    if i=='U':
        u+=1
    if i=='D':
        d+=1
    if i=='R':
        r+=1
    if i=='L':
        l+=1
if l==r and u==d:
    print('True')
else:
    print('False')