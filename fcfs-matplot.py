from matplotlib import pyplot as plt
def fcfs(sequece,start):
    temp=sequence.copy()
    temp.insert(0,start)
    plt.rcParams['xtick.bottom']=plt.rcParams['xtick.labelbottom']=False
    plt.rcParams['xtick.top']=plt.rcParams['xtick.labeltop']=True
    size=len(temp)
    x=temp
    y=[]
    headmovement=0
    for i in range(0,size):
        y.append(-i)
        if i!=size-1:
            headmovement=headmovement+abs(temp[i]-temp[i+1])
    string="Headmovement=",str(headmovement)
    stirng2=str(temp)
    print(headmovement)
    plt.plot(x,y, color="green",
             markerfacecolor="blue",
             marker="o",
             markersize=5,linewidth=2,
             label="FCFS")
    plt.ylim=(0,size)
    plt.yticks([])
    plt.xlim=(0,199)
    plt.title("fcfs")
    plt.show()
                    
                
                
if __name__=='__main__':
    sequence=list(map(int,input("ENTER THE SEQUENCE:").strip().split()))
    head=50
    fcfs(sequence,head)