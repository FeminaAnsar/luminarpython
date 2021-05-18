size=int(input("Enter the size : "))
queue=[]

rear=0
front=0

n=1

def insertion():
    global rear
    global front
    if rear<size:
        item=int(input("Enter the element : "))
        queue.insert(rear,item)
        rear+=1
    else:
        print(rear)
        print("Queue is full...!!!")


def deletion():
    global rear
    global front
    #rear-=1
    if(rear==front):
        print("Queue is empty..!!")
    else:
        print(queue[front],"Deleted...!!")
        front+=1

def display():
    for i in range(front,rear):
        print(queue[i])

while(n!=0):
    option=int(input("Enter the Task : 1)INSERT  2)DELETE 3)DISPLAY "))
    if(option==1):
        insertion()
    elif(option==2):
        deletion()
    elif(option==3):
        display()
    else:
        print("Invalid option entered...!!!!")
    n=int(input("EXIT==press'0'   CONTINUE==press any key"))