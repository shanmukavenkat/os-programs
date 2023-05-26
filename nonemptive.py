pro=int(input("enter no of processes:"))
p=[0]*pro
for i in range(pro):
    p[i]=tuple(map(int,input("enter pid,arrival time,burst time:").split()))
ct=[0]*pro
tat=[0]*pro
wt=[0]*pro
for i in range(pro):
    if p[0][0]:
      ct[i]=p[i][1]+p[i][2]
      tat[i]=p[i][1]+p[i][2]
      wt[i]=p[i][1]+p[i][2]
    else:
        for i in range(1,pro):
            sort(p[i][0])
        ct[i]=p[i-1][1]+p[i][2]
        tat[i]=ct[i]-p[i][2]
        wt[i]=tat[i]-p[i][1]
             
    
print(ct)
print(tat)
print(wt)
        
        