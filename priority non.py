n=int(input("enter no of processes:"))
print("enter the process id,burst time and priority:")
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l[i][2].sort()
ct=0
for i in range(n):
    ct+=l[i][1]
    l[i].append(ct)
tat,wt=0,0
print("pid bt p ct tat wt")
for i in range(n):
    print(l[i][0]," ",l[i][1]," ",l[i][2]," ",l[i][3]," ",l[i][3]," ",l[i][3]-l[i][1])
ttat,twt=0,0
for i in range(n):
    ttat+=l[i][3]
    twt+=(l[i][3]-l[i][1])
print("avg tat:",ttat/n)
print("avg wt:",twt/n)




