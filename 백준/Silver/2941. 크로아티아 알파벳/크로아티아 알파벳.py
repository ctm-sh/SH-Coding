a=input()
d = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
for j in a:
    for i in d:        
        if i in a:
            a=a.replace(i,' ',1)
            cnt+=1
            break
a=a.replace(' ','')
print(len(a)+cnt)