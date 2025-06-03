a = input()
cnt=0
for i in range(len(a)//2):
    if a[i]==a[-i-1]:
        cnt+=1
    else:
        print(0)
        break
if cnt==len(a)//2:
    print(1)