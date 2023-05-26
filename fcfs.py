def fcfs(p):
    ct=[0]*len(p)
    tat=[0]*len(p)
    wt=[0]*len(p)
    print(f"pid \t arrival time \t burst time \t complete time \t turn around time \t waiting time")
    for i in range(len(p)):
        ct[i]=ct[i-1]+p[i][2]
        tat[i]=ct[i-1]-p[i][1]+p[i][2]
        wt[i]=tat[i]-p[i][2]
        print(f"{p[i][0]} \t {p[i][1]} \t\t {p[i][2]} \t\t {ct[i]} \t\t {tat[i]} \t\t\t\t {wt[i]}\t")
        print(f"avg tat:{sum(tat)/len(p)}")
        print(f"avg wt:{sum(wt)/len(p)}")
n=int(input("enter no of processes:"))
p=[0]*n
for i in range(n):
    p[i]=tuple(map(int,input("enter pid,arrival time,burst time:").split()))
fcfs(p)
